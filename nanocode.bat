@echo off
title nanocode Launcher
setlocal

:: Check if .env exists
if not exist ".env" (
    echo [!] .env file not found.
    if exist ".env.example" (
        echo [i] Copying .env.example to .env ...
        copy .env.example .env
        echo [!] Please edit .env and add your OPENROUTER_API_KEY.
        pause
        exit /b
    ) else (
        echo [!] .env.example also not found. Please create a .env file with OPENROUTER_API_KEY.
        pause
        exit /b
    )
)

:: Run launcher
python launcher.py
pause
