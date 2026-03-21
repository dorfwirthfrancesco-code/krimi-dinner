@echo off
chcp 65001 >nul
title Krimi Dinner

echo.
echo  Krimi Dinner wird gestartet...
echo.

py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo  FEHLER: Python nicht gefunden.
        echo  Bitte Python von https://python.org installieren.
        echo  Beim Installieren "Add Python to PATH" aktivieren.
        pause
        exit /b 1
    )
    set PYTHON=python
) else (
    set PYTHON=py
)

echo  Installiere Abhaengigkeiten...
%PYTHON% -m pip install flask --quiet

echo  Starte Server...
echo.
echo  App laeuft auf: http://localhost:5000
echo  Beenden mit STRG+C
echo.

start "" /b cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:5000"

%PYTHON% app.py

pause
