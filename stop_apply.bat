@echo off
setlocal EnableExtensions
echo Stopping boss-auto-apply python processes...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | Where-Object { ($_.CommandLine -match 'boss-auto-apply') -and ($_.CommandLine -match 'boss_auto_apply') } | ForEach-Object { Write-Host ('STOP PID ' + $_.ProcessId + ' ' + $_.CommandLine); Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }"
set PY=python
if exist "%~dp0.venv\Scripts\python.exe" set PY=%~dp0.venv\Scripts\python.exe
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"
"%PY%" -u -B -m boss_auto_apply.cli.run_lock release
if not "%BOSS_DASHBOARD_LAUNCH%"=="1" pause
