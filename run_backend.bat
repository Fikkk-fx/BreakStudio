@echo off
title BreakStudio Backend
echo ===================================================
echo   BreakStudio - Backend Server (FastAPI)
echo ===================================================
echo API Running at: http://localhost:8000
echo API Docs at:    http://localhost:8000/docs
echo.
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
pause
