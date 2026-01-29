# Code Documentation - Nanocode

Nanocode is a minimal agentic coding assistant designed for simplicity and safety. This document details its technical architecture and implementation.

## 1. File & Folder Structure

- `nanocode.py`: The core agentie engine containing the main loop, API integration, and tool implementations.
- `launcher.py`: Portable entry point that handles absolute path resolution for its dependencies.
- `bin/cli.js`: Node.js wrapper that allows `nanocode` to be run as a global command from any directory.
- `nanocode.bat` / `nanocode.sh`: OS-specific launchers.
- `.env.example`: Template for environment variables.
- `LICENSE`: GPL v3 license file.
- `README.md` / `CODE_DOCUMENTATION.md` / `DESIGN_PHILOSOPHY.md` / `CONTRIBUTING.md`: Documentation suite.
- `RELEASE_NOTES.md` / `SOCIAL_MEDIA.md`: Release and marketing assets.

## 2. High-Level Architecture

Nanocode follows a decoupled design where the core agent logic is separated from the model selection and environment setup phases.

### A. Launch & Selection Phase
1. **Discovery**: `fetch_models.py` queries OpenRouter's API to find models with zero cost.
2. **Selection**: `launcher.py` displays these models in a balanced, two-column layout with a "half and half" split for high information density. Long model names are automatically truncated to ensure UI stability.
3. **Bootstrapping**: The launcher resolves absolute paths for the project root to ensure `.env` and `nanocode.py` are found even when the current working directory is external. It then spawns the main `nanocode.py` process.

### B. Core Agentic Loop (`nanocode.py`)
The engine operates in a continuous loop:
- **Smart Indexing**: On startup, the engine performs a recursive directory scan (ignoring standard meta-folders) to build a project tree. This is injected as context to minimize exploratory `glob` calls.
- **Input**: User provides a prompt or uses a command like `/fix`.
- **Model Call**: Request sent to Claude (Anthropic) or any model via OpenRouter. The system prompt instructs the model on multi-tool batching.
- **Tool Parsing**: If the model response includes one or more `tool_use` blocks, the engine intercepts them for sequential execution.
- **Human Approval**: For `write`, `edit`, and `bash`, the user must approve the action after seeing a diff or command preview.
- **Execution**: Tool runs in the user's *current* terminal directory. tool results are fed back to the model.
- **Final Output**: The loop ends when the model provides a text response without further tool calls.

## 3. Core Modules & Functions

| Function | Module | Description |
|----------|--------|-------------|
| `call_api` | `nanocode.py` | Handles HTTPS requests to OpenRouter/Anthropic. |
| `confirm_diff` | `nanocode.py` | Generates and displays colored diffs for user approval. |
| `run_tool` | `nanocode.py` | Routes tool requests to their respective implementations. |
| `fetch_free_models`| `fetch_models.py` | Parses OpenRouter model pricing data. |
| `main` | `nanocode.py` | Manages the conversation state and agentic loop. |

## 4. Data Flow

```
User Input -> [nanocode.py] -> OpenRouter/Anthropic API 
                                      |
                                [Tool Use Request]
                                      |
                         [Safety Check (Diff/Approval)]
                                      |
                             [Local Tool Execution]
                                      |
                                [Tool Output] -> (Back to API)
```

## 5. Execution Flow

1. **Launch**: `nanocode.bat` -> `launcher.py` -> `nanocode.py`.
2. **Initialization**: Load `.env` -> Fetch Models -> Select Model.
3. **Interactive Session**:
   - User enters command (e.g., "create a readme").
   - AI requests `write(path="README.md", content="...")`.
   - `confirm_diff` displays the diff.
   - User types `y`.
   - File is written.
   - AI confirms completion.

## 6. Dependencies
- **Runtime**: Python 3.x
- **Included Standard Libraries**: `difflib`, `glob`, `json`, `os`, `platform`, `re`, `subprocess`, `sys`, `urllib`.
- **External Dependencies**: **None**.
