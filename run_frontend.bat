@echo off
title BreakStudio Frontend
echo ===================================================
echo   BreakStudio - Frontend (Vite + React)
echo ===================================================
echo Web UI Running at: http://localhost:5173
echo.
cd /d "%~dp0frontend"
cmd /c npm.cmd run dev
pause
