#!/usr/bin/env python3
"""nanocode - minimal claude code alternative"""

import difflib, glob as globlib, json, os, platform, re, subprocess, sys, urllib.request

# Load .env file from the script's directory if it exists
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v)

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/messages" if OPENROUTER_KEY else "https://api.anthropic.com/v1/messages"
MODEL = os.environ.get("MODEL", "anthropic/claude-opus-4.5" if OPENROUTER_KEY else "claude-opus-4-5")
INCLUDE_REASONING = os.environ.get("INCLUDE_REASONING", "false").lower() == "true"

# ANSI colors
RESET, BOLD, DIM = "\033[0m", "\033[1m", "\033[2m"
BLUE, CYAN, GREEN, YELLOW, RED = (
    "\033[34m",
    "\033[36m",
    "\033[32m",
    "\033[33m",
    "\033[31m",
)
L_GREEN, L_RED, GRAY = "\033[92m", "\033[91m", "\033[90m"


def confirm_diff(path, old_text, new_text):
    if old_text == new_text:
        return True
    print(f"\n{BOLD}{YELLOW}Proposed changes to {path}:{RESET}")
    diff = list(difflib.unified_diff(
        old_text.splitlines(keepends=True),
        new_text.splitlines(keepends=True),
        fromfile=f"a/{path}", tofile=f"b/{path}"
    ))
    for line in diff:
        if line.startswith("+"): print(f"{L_GREEN}{line.rstrip()}{RESET}")
        elif line.startswith("-"): print(f"{L_RED}{line.rstrip()}{RESET}")
        else: print(f"{DIM}{line.rstrip()}{RESET}")
    return input(f"\n{BOLD}Approve? (y/n): {RESET}").lower() == "y"


def read(args):
    lines = open(args["path"]).readlines()
    offset = args.get("offset", 0)
    limit = args.get("limit", len(lines))
    selected = lines[offset : offset + limit]
    return "".join(f"{offset + idx + 1:4}| {line}" for idx, line in enumerate(selected))


def write(args):
    path = args["path"]
    new_content = args["content"]
    old_content = open(path).read() if os.path.exists(path) else ""
    if not confirm_diff(path, old_content, new_content):
        return "error: user rejected change"
    with open(path, "w") as f:
        f.write(new_content)
    return "ok"


def edit(args):
    path = args["path"]
    text = open(path).read()
    old, new = args["old"], args["new"]
    if old not in text:
        return "error: old_string not found"
    count = text.count(old)
    if not args.get("all") and count > 1:
        return f"error: old_string appears {count} times, must be unique (use all=true)"
    replacement = (
        text.replace(old, new) if args.get("all") else text.replace(old, new, 1)
    )
    if not confirm_diff(path, text, replacement):
        return "error: user rejected change"
    with open(path, "w") as f:
        f.write(replacement)
    return "ok"


def glob(args):
    pattern = (args.get("path", ".") + "/" + args["pat"]).replace("//", "/")
    files = globlib.glob(pattern, recursive=True)
    files = sorted(
        files,
        key=lambda f: os.path.getmtime(f) if os.path.isfile(f) else 0,
        reverse=True,
    )
    return "\n".join(files) or "none"


def grep(args):
    pattern = re.compile(args["pat"])
    hits = []
    for filepath in globlib.glob(args.get("path", ".") + "/**", recursive=True):
        try:
            for line_num, line in enumerate(open(filepath), 1):
                if pattern.search(line):
                    hits.append(f"{filepath}:{line_num}:{line.rstrip()}")
        except Exception:
            pass
    return "\n".join(hits[:50]) or "none"


def bash(args):
    cmd = args["bash"] if "bash" in args else args.get("cmd", "")
    if not cmd: return "error: no command"
    print(f"\n{BOLD}{YELLOW}Run command: {RESET}{cmd}")
    if input(f"{BOLD}Approve? (y/n): {RESET}").lower() != "y":
        return "error: user rejected command"
    proc = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True
    )
    output_lines = []
    try:
        while True:
            line = proc.stdout.readline()
            if not line and proc.poll() is not None:
                break
            if line:
                print(f"  {DIM}│ {line.rstrip()}{RESET}", flush=True)
                output_lines.append(line)
        proc.wait(timeout=30)
    except subprocess.TimeoutExpired:
        proc.kill()
        output_lines.append("\n(timed out after 30s)")
    return "".join(output_lines).strip() or "(empty)"


# --- Tool definitions: (description, schema, function) ---

TOOLS = {
    "read": (
        "Read file with line numbers (file path, not directory)",
        {"path": "string", "offset": "number?", "limit": "number?"},
        read,
    ),
    "write": (
        "Write content to file",
        {"path": "string", "content": "string"},
        write,
    ),
    "edit": (
        "Replace old with new in file (old must be unique unless all=true)",
        {"path": "string", "old": "string", "new": "string", "all": "boolean?"},
        edit,
    ),
    "glob": (
        "Find files by pattern, sorted by mtime",
        {"pat": "string", "path": "string?"},
        glob,
    ),
    "grep": (
        "Search files for regex pattern",
        {"pat": "string", "path": "string?"},
        grep,
    ),
    "bash": (
        "Run shell command",
        {"cmd": "string"},
        bash,
    ),
}


def run_tool(name, args):
    try:
        return TOOLS[name][2](args)
    except Exception as err:
        return f"error: {err}"


def make_schema():
    result = []
    for name, (description, params, _fn) in TOOLS.items():
        properties = {}
        required = []
        for param_name, param_type in params.items():
            is_optional = param_type.endswith("?")
            base_type = param_type.rstrip("?")
            properties[param_name] = {
                "type": "integer" if base_type == "number" else base_type
            }
            if not is_optional:
                required.append(param_name)
        result.append(
            {
                "name": name,
                "description": description,
                "input_schema": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            }
        )
    return result


def call_api(messages, system_prompt):
    payload = {
        "model": MODEL,
        "max_tokens": 8192,
        "system": system_prompt,
        "messages": messages,
        "tools": make_schema(),
    }
    if INCLUDE_REASONING and OPENROUTER_KEY:
        payload["include_reasoning"] = True

    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",
            **({"Authorization": f"Bearer {OPENROUTER_KEY}"} if OPENROUTER_KEY else {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", "")}),
        },
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read())


def separator():
    return f"{DIM}{'─' * min(os.get_terminal_size().columns, 80)}{RESET}"


def render_markdown(text):
    return re.sub(r"\*\*(.+?)\*\*", f"{BOLD}\\1{RESET}", text)


def get_project_tree():
    """Generates a condensed project tree for context."""
    ignore = {'.git', 'node_modules', '__pycache__', '.venv'}
    tree = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignore]
        level = root.replace('.', '').count(os.sep)
        indent = '  ' * level
        base = os.path.basename(root)
        if base:
            tree.append(f"{indent}📁 {base}/")
        for f in files:
            tree.append(f"{indent}  📄 {f}")
    return "\n".join(tree[:100]) # Limit to top 100 items


def main():
    print(f"{BOLD}nanocode{RESET} | {DIM}{MODEL} ({'OpenRouter' if OPENROUTER_KEY else 'Anthropic'}) | {os.getcwd()}{RESET}\n")
    messages = []
    
    # Feature 1: Get Project Tree for initial context
    tree = get_project_tree()
    system_prompt = (
        f"Concise coding assistant. cwd: {os.getcwd()}\n"
        f"Project Structure:\n{tree}\n\n"
        "Guidelines:\n"
        "1. Favor 'edit' over 'write' for small changes.\n"
        "2. You can call multiple tools in one turn for complex multi-file changes (Batching).\n"
        "3. If a task requires multiple steps, explain the plan briefly first."
    )

    while True:
        try:
            print(separator())
            user_input = input(f"{BOLD}{BLUE}❯{RESET} ").strip()
            print(separator())
            if not user_input:
                continue
            if user_input in ("/q", "exit", "quit"):
                break
            if user_input == "/c":
                messages = []
                print(f"{GREEN}⏺ Cleared conversation{RESET}")
                continue
            if user_input == "/h":
                print(f"{BOLD}Commands:{RESET}")
                print("  /c    - Clear conversation")
                print("  /q    - Quit")
                print("  /s    - System Info")
                print("  /save - Save conversation")
                print("  /fix  - Analyze last error and fix it")
                print("  /h    - Help")
                continue
            if user_input == "/s":
                print(f"{BOLD}System Info:{RESET}")
                print(f"  OS: {platform.system()} {platform.release()}")
                print(f"  Python: {sys.version.split()[0]}")
                print(f"  Directory: {os.getcwd()}")
                print(f"  Model: {MODEL}")
                print(f"  Reasoning: {'Enabled' if INCLUDE_REASONING else 'Disabled'}")
                continue
            if user_input == "/save":
                import time
                filename = f"chat_{int(time.time())}.json"
                with open(filename, "w") as f:
                    json.dump(messages, f, indent=2)
                print(f"{GREEN}⏺ Saved conversation to {filename}{RESET}")
                continue
            
            # Feature 3: Fix command
            if user_input.startswith("/fix"):
                error_context = user_input[4:].strip()
                if not error_context:
                    error_context = "Check the last tool output for errors or terminal state and fix it."
                user_input = f"CRITICAL: There is an error. Please analyze and fix it: {error_context}"

            messages.append({"role": "user", "content": user_input})

            # agentic loop: keep calling API until no more tool calls
            while True:
                response = call_api(messages, system_prompt)
                
                # Feature: Display reasoning/thinking if present (OpenRouter)
                reasoning = response.get("reasoning")
                if reasoning:
                    print(f"\n{GRAY}💭 Thinking: {reasoning.strip()}{RESET}")

                content_blocks = response.get("content", [])
                tool_results = []

                for block in content_blocks:
                    if block["type"] == "text":
                        print(f"\n{CYAN}⏺{RESET} {render_markdown(block['text'])}")
                    
                    # Handle thinking/reasoning blocks if they come in content
                    elif block["type"] in ("reasoning", "thought", "thinking"):
                        print(f"\n{GRAY}💭 Thinking: {block.get('text', block.get('reasoning', '')).strip()}{RESET}")

                    if block["type"] == "tool_use":
                        tool_name = block["name"]
                        tool_args = block["input"]
                        arg_preview = str(list(tool_args.values())[0])[:50]
                        print(
                            f"\n{GREEN}⏺ {tool_name.capitalize()}{RESET}({DIM}{arg_preview}{RESET})"
                        )

                        result = run_tool(tool_name, tool_args)
                        result_lines = result.split("\n")
                        preview = result_lines[0][:60]
                        if len(result_lines) > 1:
                            preview += f" ... +{len(result_lines) - 1} lines"
                        elif len(result_lines[0]) > 60:
                            preview += "..."
                        print(f"  {DIM}⎿  {preview}{RESET}")

                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": block["id"],
                                "content": result,
                            }
                        )

                messages.append({"role": "assistant", "content": content_blocks})

                if not tool_results:
                    break
                messages.append({"role": "user", "content": tool_results})

            print()

        except (KeyboardInterrupt, EOFError):
            break
        except Exception as err:
            print(f"{RED}⏺ Error: {err}{RESET}")


if __name__ == "__main__":
    main()
