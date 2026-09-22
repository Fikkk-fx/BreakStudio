@echo off
title BreakStudio Launcher
echo ===================================================
echo   Starting BreakStudio Web Studio
echo ===================================================
echo [1/2] Starting Backend (FastAPI :8000)...
start "BreakStudio Backend" cmd /k "python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload"
timeout /t 2 /nobreak >nul

echo [2/2] Starting Frontend (Vite :5173)...
start "BreakStudio Frontend" cmd /k "cd /d "%~dp0frontend" && npm.cmd run dev"
timeout /t 3 /nobreak >nul

echo.
echo Opening browser at http://localhost:5173 ...
start http://localhost:5173
echo BreakStudio started successfully!
