#!/bin/bash

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "[!] .env file not found."
    if [ -f ".env.example" ]; then
        echo "[i] Copying .env.example to .env ..."
        cp .env.example .env
        echo "[!] Please edit .env and add your OPENROUTER_API_KEY."
        exit 1
    else
        echo "[!] .env.example also not found. Please create a .env file with OPENROUTER_API_KEY."
        exit 1
    fi
fi

# Run launcher
python3 launcher.py
