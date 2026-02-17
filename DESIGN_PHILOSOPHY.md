# Design Philosophy - Nanocode

Nanocode exists at the intersection of powerful AI agency and radical user safety.

## 1. Problem Definition
Traditional AI coding assistants either force users into a "black box" agentic loop where they lose control over their filesystem, or they are too heavy, requiring complex environments, Docker, or multiple `pip install` dependencies. This creates a barrier to entry and a risk for local development.

## 2. Why Nanocode?
Nanocode was built to provide a **transparent, single-file alternative** that gives users the power of an agentic loop without sacrificing safety or ease of use. It solves the "trust problem" by making every AI action visible and reversible before it hits the disk.

## 3. Design Principles
- **Safety First**: "Human-in-the-loop" is not an optional feature; it is the core architecture. Every modification must be approved.
- **Radical Minimalism**: Use only what Python provides by default. No external libraries, no complex abstractions.
- **Location Agnostic**: The tool should work precisely the same whether run inside its installation folder or globally via a system PATH. Your data stays where you run the tool.
- **Instant Context**: Use lightweight, non-indexed scans to give the AI a "head start" without the overhead of heavy background indexing services.
- **Information Density**: Deliver maximum utility with minimal UI friction. Our multi-column, truncated model selection ensures large sets of data are consumed quickly and cleanly.
- **Accessibility**: Support free models by default. To address the "noise" in the free model ecosystem, we use capability-based discovery (filtering by Tools, Vision, etc.) so users can find the most capable free models instantly.

## 4. Target Audience & Use Cases
- **Audience**: Developers who want a lightweight, local assistant they can trust; students learning AI interactions; and power users who need a quick "Swiss Army Knife" for codebase exploration.
- **Use Cases**: Quick refactors, documentation generation, automated log analysis, and global codebase maintenance.

## 5. Real-World Workflow Fit
Nanocode is designed to be "launched and forgotten." It respects your `cwd` (Current Working Directory). You use it as a powerful companion—go to any project folder on your machine, type `nanocode`, let it handle a task, and then close it. The cross-platform launchers and Node integration ensure this "global utility" feel.

## 6. Trade-offs & Constraints
- **Scope**: Nanocode is not an IDE. It focuses on the agentic loop and file/terminal tools.
- **Model Choice**: While it supports any OpenRouter model, it is optimized for the tool-calling formats of Anthropic's Claude models.
- **Capacity**: For extremely large codebases (millions of lines), the local `grep` and `glob` tools might be slower than specialized indexing tools used in heavy IDEs.
