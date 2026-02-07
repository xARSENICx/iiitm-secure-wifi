# IIITM Secure Wi-Fi (Unofficial)

Community-maintained one-click Wi-Fi onboarding packages for IIITM students.

**Maintainer:** Ayush Sah ([imt_2022026@iiitm.ac.in](mailto:imt_2022026@iiitm.ac.in))

This repository provides configuration files and packages to automatically set up **IIITM_Secure** and **IIITM_Secure_5G** on your devices.

## Download & Install

## One-Click Setup (CLI Tool)

The easiest way to set up everything is using our simple CLI tool. It works on macOS, Linux, and Windows.

```bash
# Run the setup tool
python3 cli/main
```

## Manual Installation (OS Specific)

If you prefer not to use the terminal, you can still use the packages:

- **[macOS & iOS](./macos-ios/)**: Download and install the `.mobileconfig` profile.
- **[Windows](./windows/)**: Download and run the setup utility.
- **[Linux](./linux/)**: Install the `.deb` or `.rpm` package.

## Android Setup (Manual)

Android does not allow silent configuration. Follow these steps:

1. Download **[IIITM-CA.crt](./certs/IIITM-CA.crt)**.
2. Go to **Settings** > **Security** > **Install a certificate** > **Wi-Fi Certificate**.
3. Select the downloaded file and name it `IIITM-WiFi`.
4. Connect to **IIITM_Secure** / **IIITM_Secure_5G** with these settings:
   - **EAP Method**: `TTLS`
   - **Phase 2 Authentication**: `PAP`
   - **CA Certificate**: Select `IIITM-WiFi`
   - **Domain**: `iiitm.ac.in`
   - **Identity**: Your LDAP Username
   - **Password**: Your LDAP Password

## Security Features

- **WPA2/WPA3-Enterprise**: Industry-standard encryption.
- **EAP-TTLS + PAP**: Secure authentication tunnel.
- **CA Certificate Validation**: Prevents "Man-in-the-Middle" attacks by verifying the server.
- **Native Storage**: Credentials are stored securely by your OS (Keychain/Credential Manager).

## Support

This is an **unofficial** community project. If you encounter any issues, please open an issue on this repository or contact **Ayush Sah** at [imt_2022026@iiitm.ac.in](mailto:imt_2022026@iiitm.ac.in). For infrastructure-level issues (like password resets), contact the **IIITM Network Cell**.
