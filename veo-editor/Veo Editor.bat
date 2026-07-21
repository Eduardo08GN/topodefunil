@echo off
setlocal
title Veo Editor By EDDIE
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo   Ambiente nao encontrado. Rode "instalar.bat" primeiro.
    echo.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" app.py
pause
