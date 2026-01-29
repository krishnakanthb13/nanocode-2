# Design Philosophy - Nanocode

Nanocode exists at the intersection of powerful AI agency and radical user safety.

## 1. Problem Definition
Traditional AI coding assistants either force users into a "black box" agentic loop where they lose control over their filesystem, or they are too heavy, requiring complex environments, Docker, or multiple `pip install` dependencies. This creates a barrier to entry and a risk for local development.

## 2. Why Nanocode?
Nanocode was built to provide a **transparent, single-file alternative** that gives users the power of an agentic loop without sacrificing safety or ease of use. It solves the "trust problem" by making every AI action visible and reversible before it hits the disk.

## 3. Design Principles
- **Safety First**: "Human-in-the-loop" is not an optional feature; it is the core architecture. Every modification must be approved.
- **Radical Minimalism**: Use only what Python provides by default. No external libraries, no complex abstractions.
- **Maximum Transparency**: The code is short enough (~300 lines) for a developer to read and audit in minutes.
- **Accessibility**: Support free models by default to ensure anyone with an internet connection can use agentic AI for coding.

## 4. Target Audience & Use Cases
- **Audience**: Developers who want a lightweight, local assistant they can trust; students learning AI interactions; and power users who need a quick "Swiss Army Knife" for codebase exploration.
- **Use Cases**: Quick refactors, documentation generation, automated log analysis, and local codebase search.

## 5. Real-World Workflow Fit
Nanocode is designed to be "launched and forgotten." It doesn't take over your entire workflow. You use it as a powerful companion—launch it in a specific folder, let it handle a task (like "add docstrings to all files"), and then close it. The cross-platform launchers (`.bat` and `.sh`) make this "task-on-demand" workflow frictionless.

## 6. Trade-offs & Constraints
- **Scope**: Nanocode is not an IDE. It focuses on the agentic loop and file/terminal tools.
- **Model Choice**: While it supports any OpenRouter model, it is optimized for the tool-calling formats of Anthropic's Claude models.
- **Capacity**: For extremely large codebases (millions of lines), the local `grep` and `glob` tools might be slower than specialized indexing tools used in heavy IDEs.
