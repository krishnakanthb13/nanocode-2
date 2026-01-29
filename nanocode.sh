#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if .env exists
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "[!] .env file not found in $SCRIPT_DIR."
    if [ -f "$SCRIPT_DIR/.env.example" ]; then
        echo "[i] Copying .env.example to .env ..."
        cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
        echo "[!] Please edit .env and add your OPENROUTER_API_KEY."
        exit 1
    else
        echo "[!] .env.example also not found. Please create a .env file with OPENROUTER_API_KEY."
        exit 1
    fi
fi

# Run launcher
python3 "$SCRIPT_DIR/launcher.py"
