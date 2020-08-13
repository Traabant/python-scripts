@echo off
setlocal

cd /D "%~dp0"
powershell -NoProfile -ExecutionPolicy bypass -Command "& {.\file_size.ps1 ; exit $LastExitCode }"
pause