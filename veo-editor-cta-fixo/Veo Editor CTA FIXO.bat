@echo off
setlocal
title Veo Editor CTA FIXO
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo   Ambiente nao encontrado. Rode "instalar.bat" primeiro.
    echo.
    pause
    exit /b 1
)

start "" ".venv\Scripts\pythonw.exe" app.py
exit /b 0