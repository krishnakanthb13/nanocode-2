# Code Documentation - Nanocode

Nanocode is a minimal agentic coding assistant designed for simplicity and safety. This document details its technical architecture and implementation.

## 1. File & Folder Structure

- `nanocode.py`: The core agentie engine containing the main loop, API integration, and tool implementations.
- `launcher.py`: Entry point for user-friendly startup and model selection.
- `fetch_models.py`: Utility script to fetch and filter free models from OpenRouter.
- `nanocode.bat` / `nanocode.sh`: OS-specific launchers.
- `.env.example`: Template for environment variables.
- `LICENSE`: GPL v3 license file.
- `README.md` / `CODE_DOCUMENTATION.md` / `DESIGN_PHILOSOPHY.md` / `CONTRIBUTING.md`: Documentation suite.
- `RELEASE_NOTES.md` / `SOCIAL_MEDIA.md`: Release and marketing assets.

## 2. High-Level Architecture

Nanocode follows a decoupled design where the core agent logic is separated from the model selection and environment setup phases.

### A. Launch & Selection Phase
1. **discovery**: `fetch_models.py` queries OpenRouter's API to find models with zero cost.
2. **Selection**: `launcher.py` displays these models and allows the user to pick one.
3. **Bootstrapping**: The launcher sets up the environment (using `.env` or defaults) and spawns the main `nanocode.py` process.

### B. Core Agentic Loop (`nanocode.py`)
The engine operates in a continuous loop:
- **Input**: User provides a prompt.
- **Model Call**: Request sent to Claude (Anthropic) or any model via OpenRouter.
- **Tool Parsing**: If the model response includes a `tool_use` request, the engine intercepts it.
- **Human Approval**: For `write`, `edit`, and `bash`, the user must approve the action after seeing a diff or command preview.
- **Execution**: Tool runs locally, and results are fed back to the model.
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
