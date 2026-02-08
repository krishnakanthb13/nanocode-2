# Release Notes - nanocode

All notable changes to this project will be documented in this file.
 
## [v0.0.8] - 2026-01-29
### "UI & Density Update" - UX Enhancements
 
This update focuses on improving the startup experience and information presentation.
 
### 🚀 New Features & Enhancements
- **Balanced Model Selection**: The free model list is now displayed in a balanced, two-column "half and half" layout, making it much easier to scan through large sets of models.
- **Improved Information Density**: Long model names are automatically truncated to ensure the terminal UI remains stable and professional, avoiding line wraps.
- **Quick Exit**: Added a dedicated `0` option to the model selection menu, allowing for an instant exit if you change your mind during launch.
- **Terminal Alignment**: Refined spacing and alignment for a cleaner, premium terminal aesthetic.
- **Documentation Sync**: Updated project documentation to reflect the new design principles and information density standards.
 
---
 
## [v0.0.7] - 2026-01-29
### "The Global Agent" - Feature Update

This update transforms **nanocode** into a truly portable and smarter assistant.

### 🚀 New Features
- **True Portability**: Run `nanocode` from any directory on your system. It now respects your Current Working Directory (CWD) while keeping its own "brain" and settings relative to its installation.
- **Smart Context (Auto-Indexing)**: Upon startup, the agent automatically builds a map of your project structure, giving the AI immediate visibility into your codebase.
- **Multi-File Batching**: The agent can now plan and execute complex, multi-file changes in a single conversational turn.
- **Global Command Integration**: Includes `npm link` support to make `nanocode` a first-class citizen in your terminal.
- **Removed Shell Warning**: Updated the Node.js wrapper to eliminate security warnings and process overhead.

### 🛠 New Commands
- `/fix`: A dedicated command to analyze terminal errors or broken code and propose immediate repairs.
- `/save`: Export your entire agentic conversation to a JSON timestamped file.

---


## [v0.0.1] - 2026-01-29

### 🚀 Initial Release
The first public version of **nanocode**, a minimal, zero-dependency Claude Code alternative focused on transparency and safety.

### ✨ Key Features
- **Agentic Loop**: Full reasoning and execution loop for coding tasks.
- **Human-in-the-Loop Safety**: All file writes, edits, and shell commands require manual `y/n` confirmation.
- **Colored Diffs**: Integrated preview of changes using light green (additions) and light red (deletions).
- **Free Model Selector**: Interactively pick current free models from OpenRouter on launch.
- **Cross-Platform Launchers**: One-click startup with `nanocode.bat` (Windows) and `nanocode.sh` (Linux/Mac).
- **Zero Dependencies**: Runs on standard Python 3.x libraries—no `pip install` required.

### 🛠️ Included Tools
- `read`: View files with line numbers.
- `write` & `edit`: Modify files with mandatory diff approval.
- `glob` & `grep`: Search for files and code patterns.
- `bash`: Execute shell commands with manual approval.

### � Commands
- `/s`: System diagnostics (OS, Python, active Model).
- `/save`: Export session history to JSON.
- `/h`: Help menu.
- `/c`: Clear session.

---

## Complete Feature Overview (v0.0.7)
This section summarizes all capabilities included in the initial launch phase of **nanocode**.

### 🧠 Intelligence & Context
- **Smart Agent Loop**: A continuous cycle of reasoning, tool selection, and execution.
- **Smart Context (Auto-Indexing)**: Instantly scans your project tree on startup so the AI doesn't have to "explore" to find your files.
- **Multi-File Batching**: The AI can plan and perform edits across multiple files in a single response turn.

### 🛡️ Radical Safety (Human-in-the-Loop)
- **Unified Diff Previews**: Every file change is shown in the terminal with colored ANSI highlights (Green for additions, Red for deletions).
- **Mandatory Approval**: No file is written, and no command is run without the user typing `y`.
- **Sandbox-like Execution**: All operations occur in your local directory under your direct supervision.

### 🌍 Portability & Speed
- **Global Utility**: `npm link` support allows you to run `nanocode` in any folder on your machine.
- **Zero Dependencies**: Pure Python 3. Does not require `pip`, `conda`, or any external package managers.
- **Cross-Platform**: Native launchers for Windows (`.bat`) and Unix/Mac (`.sh`).

### 🔧 Tools & Commands
- **Core Tools**: `read` (with line numbers), `write`, `edit` (string replacement), `glob` (file search), `grep` (regex search), and `bash` (shell access).
- **Helper Commands**:
    - `/fix`: Quickly analyze and repair terminal errors or code bugs.
    - `/save`: Export your entire session to a JSON file.
    - `/s`: View system diagnostics and active model status.
    - `/c`: Clear memory to maintain a lean context.
    - `/h`: Detailed help and command menu.

### 🆓 Accessibility
- **Free Model Scraper**: Automatically finds and ranks currently available zero-cost models on OpenRouter so you can build for free.
- **Anthropic Native Support**: Optimized for Claude 3.5 Sonnet and Opus tool-calling patterns.
