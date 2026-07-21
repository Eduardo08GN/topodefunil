@echo off
setlocal
title Veo Editor By EDDIE - Instalacao
cd /d "%~dp0"

echo.
echo   ================================================
echo     Veo Editor By EDDIE - instalacao
echo   ================================================
echo.

REM ---- Python ----
where python >nul 2>nul
if errorlevel 1 (
    echo   [ERRO] Python nao encontrado no PATH.
    echo   Instale o Python 3.10+ em https://python.org
    echo   Marque "Add python.exe to PATH" durante a instalacao.
    echo.
    pause
    exit /b 1
)
echo   [ok] Python encontrado
python --version

REM ---- FFmpeg ----
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo.
    echo   [ERRO] FFmpeg nao encontrado no PATH.
    echo   Instale com:  winget install Gyan.FFmpeg
    echo   Depois FECHE e reabra este instalador.
    echo.
    pause
    exit /b 1
)
echo   [ok] FFmpeg encontrado

REM ---- ambiente virtual ----
echo.
echo   Criando ambiente virtual...
if not exist ".venv" (
    python -m venv .venv
    if errorlevel 1 (
        echo   [ERRO] Falha ao criar o ambiente virtual.
        pause
        exit /b 1
    )
)
echo   [ok] ambiente pronto

echo.
echo   Instalando dependencias (pode levar alguns minutos)...
call ".venv\Scripts\python.exe" -m pip install --upgrade pip --quiet
call ".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo   [ERRO] Falha ao instalar as dependencias.
    pause
    exit /b 1
)
echo   [ok] dependencias instaladas

REM ---- atalho na area de trabalho ----
echo.
echo   Criando atalho na area de trabalho...
powershell -NoProfile -Command ^
  "$ws = New-Object -ComObject WScript.Shell;" ^
  "$lnk = $ws.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\Veo Editor By EDDIE.lnk');" ^
  "$lnk.TargetPath = '%~dp0Veo Editor.bat';" ^
  "$lnk.WorkingDirectory = '%~dp0';" ^
  "$lnk.IconLocation = 'shell32.dll,177';" ^
  "$lnk.Description = 'Veo Editor By EDDIE';" ^
  "$lnk.Save()"
echo   [ok] atalho criado

echo.
echo   ================================================
echo     Instalacao concluida.
echo     Abra pelo atalho "Veo Editor By EDDIE"
echo     na area de trabalho.
echo   ================================================
echo.
pause
