@echo off
title Git Cleanup - Hapus File Lama dari Tracking
echo ===================================================
echo   Menghapus file lama dari git tracking...
echo ===================================================
echo.

REM Hapus file Python yang sudah dipindah ke backend/
git rm --cached pruna_client.py 2>nul
git rm --cached prompt_auditor.py 2>nul
git rm --cached skill_rules_reader.py 2>nul
git rm --cached test_suite.py 2>nul
git rm --cached test_prompt.txt 2>nul
git rm --cached SKILL.md 2>nul

REM Hapus folder yang sudah dipindah / tidak perlu
git rm -r --cached prompts/ 2>nul
git rm -r --cached rules/ 2>nul
git rm -r --cached outputs/ 2>nul
git rm -r --cached assets/ 2>nul
git rm -r --cached test_results/ 2>nul
git rm -r --cached scratch/ 2>nul
git rm -r --cached __pycache__/ 2>nul

REM Hapus node_modules dan dist dari frontend
git rm -r --cached frontend/node_modules/ 2>nul
git rm -r --cached frontend/dist/ 2>nul

REM Hapus database dari backend
git rm --cached backend/director.db 2>nul
git rm -r --cached backend/__pycache__/ 2>nul
git rm -r --cached backend/routes/__pycache__/ 2>nul

echo.
echo ===================================================
echo   Commit dan push perubahan...
echo ===================================================
git add .
git commit -m "refactor: reorganize project structure - move all backend files to backend/, frontend to frontend/"
git push origin main

echo.
echo SELESAI! Cek Vercel dashboard untuk melihat build baru.
pause
