# Contributing to nanocode

Thank you for your interest in improving nanocode! As a project focused on minimalism and safety, we welcome contributions that align with these values.

## Bug Reports
If you find a bug, please open an issue with the following details:
- **Description**: What happened?
- **Steps to Reproduce**: How can we see the bug ourselves?
- **Expected vs Actual Behavior**: What did you expect to happen?
- **Environment**: OS, Python version, and model used.

## Feature Suggestions
We love new ideas, but we aim to keep the core `nanocode.py` under 300-400 lines. 
- Please explain the problem the new feature solves.
- Consider if it can be implemented with existing tools or minimal code.

## Development Workflow
1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/krishnakanthb13/nanocode.git
   ```
3. **Create a Branch** for your changes:
   ```bash
   git checkout -b feature/my-new-feature
   ```
4. **Implement & Test**: Ensure your changes don't break the agentic loop or safety features.
5. **Commit & Push**:
   ```bash
   git commit -m "Add feature: my new feature"
   git push origin feature/my-new-feature
   ```
6. **Open a Pull Request**: Describe your changes clearly.

## Local Development Setup
Nanocode has zero dependencies. Just ensure you have Python 3.x installed.
- Set up your `.env` file with an `OPENROUTER_API_KEY`.
- Run `launcher.py` to start the app.
- Tests can be run manually by asking the agent to perform specific file operations or shell commands.

## Pre-submission Checklist
- [ ] Code follows the minimalist style (no extra dependencies).
- [ ] Safety features (diffs/approvals) are preserved.
- [ ] Documentation (README/CODE_DOCUMENTATION) is updated if necessary.
- [ ] No sensitive credentials or keys are committed.

## Metadata
- **Main Maintainer**: Krishna Kanth B
- **GitHub**: krishnakanthb13
