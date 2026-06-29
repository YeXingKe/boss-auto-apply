@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set PY=%~dp0.venv\Scripts\python.exe
if not exist "%PY%" set PY=python
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"
"%PY%" -u -B -m boss_auto_apply.cli.status
pause
