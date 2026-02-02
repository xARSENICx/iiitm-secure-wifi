# IIITM Secure Wi-Fi - Windows Setup Script
# Run this script as Administrator to install certificates and configure Wi-Fi

# 1. Elevate to Administrator if not already
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Requesting Administrator privileges..." -ForegroundColor Yellow
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

$CurrentDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$CertPath = Join-Path $CurrentDir "..\certs\IIITM-CA.crt"
$ProfilePath = Join-Path $CurrentDir "IIITM_Secure.xml"
$Profile5GPath = Join-Path $CurrentDir "IIITM_Secure_5G.xml"

Write-Host "--- IIITM Secure Wi-Fi Configuration ---" -ForegroundColor Cyan

# 2. Install CA Certificate
if (Test-Path $CertPath) {
    Write-Host "Installing IIITM CA Certificate..." -ForegroundColor Yellow
    Import-Certificate -FilePath $CertPath -CertStoreLocation Cert:\LocalMachine\Root
    Write-Host "Success: CA Certificate installed." -ForegroundColor Green
} else {
    Write-Host "Warning: CA Certificate not found at $CertPath" -ForegroundColor Red
}

# 3. Import Wi-Fi Profiles
if (Test-Path $ProfilePath) {
    Write-Host "Configuring IIITM_Secure..." -ForegroundColor Yellow
    netsh wlan add profile filename="$ProfilePath" user=all
}

if (Test-Path $Profile5GPath) {
    Write-Host "Configuring IIITM_Secure_5G..." -ForegroundColor Yellow
    netsh wlan add profile filename="$Profile5GPath" user=all
}

Write-Host "--- Configuration Complete ---" -ForegroundColor Cyan
Write-Host "You can now connect to IIITM_Secure from your Wi-Fi menu."
Write-Host "When prompted, enter your LDAP credentials."
pause
