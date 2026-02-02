# Linux Wi-Fi Setup (Unofficial)

We provide community-maintained packages for major distributions.

## Installation

### Ubuntu / Debian / Kali (.deb)

1. Download `iiitm-secure-wifi.deb`.
2. Double-click the file to open it in the Software Center, or run:
   ```bash
   sudo dpkg -i iiitm-secure-wifi.deb
   ```

### Fedora / Red Hat / CentOS (.rpm)

1. Download `iiitm-secure-wifi.rpm`.
2. Double-click to install or run:
   ```bash
   sudo dnf install iiitm-secure-wifi.rpm
   ```

## Manual Setup (If package fails)

If you prefer manual setup, use the following settings in your Network Manager:

- **SSID**: `IIITM_Secure`
- **Security**: WPA & WPA2 Enterprise
- **Authentication**: Tunneled TLS (TTLS)
- **Inner Authentication**: PAP
- **CA Certificate**: [certs/IIITM-CA.crt](../certs/IIITM-CA.crt)
- **Username**: Your LDAP ID
- **Password**: Your LDAP Password
