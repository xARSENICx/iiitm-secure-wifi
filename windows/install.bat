@echo off
:: IIITM Wi-Fi Installer Launcher
:: This script launches the PowerShell setup with proper permissions
SET dir=%~dp0
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%dir%setup.ps1"
pause
