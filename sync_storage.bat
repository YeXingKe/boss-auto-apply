@echo off
setlocal EnableExtensions
chcp 65001 >nul
cd /d "%~dp0"

set PY=%~dp0.venv\Scripts\python.exe
if not exist "%PY%" set PY=python
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"

"%PY%" -u -B -m boss_auto_apply.services.storage
