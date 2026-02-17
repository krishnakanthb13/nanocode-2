# Social Media Announcements - v0.0.12 ("Crystal Clear Reasoning")

## 👔 LinkedIn
Headline: nanocode v0.0.12: Bringing Deep Transparency to AI Coding Tools.

I've just released v0.0.12 of nanocode, and it's all about trust and transparency. 🚀

Most AI agents are a "black box"—you see the result, but not the logic. In this update, we’re changing that.

What’s new:
💭 Thinking Process: See the model's internal reasoning in real-time. Reasoning blocks are rendered in a distinct style, showing you exactly how the AI plans its next move.
🛡️ Bash Pre-flight Checks: The agent now scans proposed commands and verifies if dependencies (like npm or git) are already in your PATH before you hit "approve."
🔍 Capability Filtering: Instantly filter the free model ecosystem on OpenRouter by Tool Calling, Vision, or Reasoning support.
🌍 Shell Awareness: Automatic detection of your OS and Shell (CMD/Bash) to ensure command compatibility.

Everything stays human-in-the-loop. Still ~300 lines of Python. Still zero external dependencies.

Check it out: https://github.com/krishnakanthb13/nanocode-2

#AI #OpenSource #DevTools #Python #CodingAssistant #Transparency

---

## 🤖 Reddit
Title: [Show HN] nanocode v0.0.12 - Watch your AI agent think in real-time + Bash Pre-flight checks.

Hey everyone,

I've just pushed v0.0.12 of **nanocode**, my minimal, zero-dependency Claude Code alternative. This release focuses on the "Human-in-the-Loop" experience.

New features:
- Display Thinking: It now renders the internal reasoning process of supported models (dimmed gray). You see the logic before the tools run.
- Dependency Verification: The bash tool now checks if a binary is installed in your PATH before asking for approval. No more "Command not found" after you approved a multi-step task!
- Rich Capability Scraper: Filter free OpenRouter models by their features (e.g., only show models that support Tool Calling or Vision).
- Shell Diagnostics: Shows OS and Shell info for every command proposal.

It remains a pure-Python, single-file engine designed for devs who want full agency without the configuration bloat.

GitHub: https://github.com/krishnakanthb13/nanocode-2

---

## 🐦 X (Twitter)
nanocode v0.0.12 is live! 🚀

Trust your tools:
💭 Real-time "Thinking" display: See the AI logic
🛡️ Bash Pre-flight: Verifies dependencies before you approve
🔍 Rich Scraper: Filter free models by Tool/Vision/Reasoning support
🌍 Shell Aware: Auto-detects OS/Shell for commands

Minimal bloat, maximum transparency. 🐍

https://github.com/krishnakanthb13/nanocode-2

---


## 👔 LinkedIn
**Headline: Introducing nanocode: The Tiny, Transparent, and Safe AI Coding Assistant.**

I'm thrilled to launch **nanocode v0.0.1**! 🚀

Most AI coding agents act as black boxes. Nanocode is different. It's a minimal, agentic tool that fits in ~300 lines of Python and prioritizes one thing: **User Control**.

Key highlights of this initial release:
✅ **Safe Agency**: Colored diffs and mandatory manual approval for every single action.
✅ **Interactive Launch**: Automatic discovery of free models on OpenRouter.
✅ **Zero Dependencies**: Pure Python 3. No install, no bloat, total transparency.

If you've been looking for a lightweight, "Human-in-the-Loop" alternative to Claude Code that you can actually trust on your local machine, check out Nanocode.

GitHub: [Link to Repo]

#AI #Coding #OpenSource #OpenRouter #Python #Productivity #v1Release

---

## 🤖 Reddit (r/programming or r/Python)
**Title: [Show HN/Reddit] nanocode - I built a 300-line, zero-dependency AI coding loop with mandatory diff approval.**

Hey everyone,

I've been working on a minimal agentic coding loop called **nanocode**. Today I'm releasing the initial version, **v0.0.1**.

The goal was to create a "Swiss Army Knife" for AI-assisted coding that doesn't require a complex setup and actually treats your filesystem with respect.

Why use it?
- **It's Safe**: It generates unified diffs for every change and waits for your `y/n`.
- **It's Free-friendly**: Includes a launcher that fetches currently available $0 models from OpenRouter.
- **It's Tiny**: Just one core file, zero `pip install` dependencies.

Architecture:
- Built using Python's `urllib`, `difflib`, and `subprocess`.
- Supports both Anthropic and OpenRouter.
- Includes `/save` for local session exports.

Check it out: [Link to Repo]
Would love to hear your thoughts on the "Human-in-the-Loop" approach!

---

## 🐦 X (Twitter)
**Introducing nanocode v0.0.1 🚀**

A minimal, agentic coding loop in ~300 lines of Python.

🛡️ Safe: Mandatory diff approval for all edits
🎨 Clear: Colored ANSI diff previews
🆓 Accessible: Interactive free-model selector for OpenRouter
🐍 Zero-dependency: Pure Python 3

AI intelligence, human control.

[Link to Repo]


---

# Social Media Announcements - v0.0.7 ("The Global Agent")

## 👔 LinkedIn
**Headline: nanocode v0.0.7: Your Portable AI Coding Partner is here.**

I've just released v0.0.7 of **nanocode**, and it's a game changer for portability and speed. 🚀

Key updates:
🌍 **Run Anywhere**: Use it as a global command in any project folder.
🧠 **Smart Context**: It scans your project tree on startup so it knows the codebase immediately.
🛠 **Batching**: Executes complex changes across multiple files in one turn.
🛡️ **Fix Mode**: New `/fix` command to instantly repair terminal errors.

Still ~300 lines of Python. Still zero dependencies. Still 100% human-in-the-loop.

## 🤖 Reddit
**Title: nanocode v0.0.7 - Smart Context, Multi-file Batching, and Global Portability.**

Hey everyone, thanks for the feedback on v0.0.1!

I've just pushed **v0.0.7** with the features you actually need for daily work:
- **Project Indexing**: It builds a tree on startup context. No more "glob" spamming.
- **Batch Operations**: It can now propose and execute multi-file edits in one go.
- **Global `npm link` support**: Move to any directory, type `nanocode`, and start building.
- **The `/fix` command**: Paste an error, and it goes to work.

## 🐦 X (Twitter)
**nanocode v0.0.7 is out! 🚀**

The tiny agent just got a brain upgrade:
📂 Portable: Works in any folder via system PATH
🌳 Smart: Auto-indexes project tree on startup
📦 Batch: Plans & edits multiple files at once
🛠 Fix: Dedicated `/fix` command for errors

Less bloat, more power. 🐍

#AI #Python #OpenSource #DevTools #Launch
