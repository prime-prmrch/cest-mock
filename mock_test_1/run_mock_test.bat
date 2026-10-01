@echo off
title Cambridge English Skills Test - Local Server
echo ========================================================
echo Cambridge English Skills Test - Mock Test 1 Local Server
echo ========================================================
echo.
echo Local Computer Access:
echo   http://localhost:8080
echo.
echo iPhone / Mobile Device Access (same Wi-Fi):
echo   http://192.168.1.20:8080
echo   (or http://192.168.1.18:8080)
echo.
echo Server is running. Press Ctrl+C in this window to stop.
echo ========================================================
echo.

cd /d "%~dp0"
start http://localhost:8080

REM Try default python, then user local path
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python -m http.server 8080
) else (
    "%LOCALAPPDATA%\Python\bin\python.exe" -m http.server 8080
)
