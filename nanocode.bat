@echo off
title nanocode Launcher
setlocal

:: Check if .env exists
if not exist "%~dp0.env" (
    echo [!] .env file not found in %~dp0.
    if exist "%~dp0.env.example" (
        echo [i] Copying .env.example to .env ...
        copy "%~dp0.env.example" "%~dp0.env"
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
python "%~dp0launcher.py"
pause
