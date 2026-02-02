# Security Policy

## Our Commitment

This project is designed to provide a secure and official way for students to connect to the IIITM Wi-Fi network. Security and privacy are our top priorities.

## Security Principles

- **No Credential Harvesting**: This project never collects, transmits, or stores your LDAP credentials. All authentication is handled directly by the operating system's native network stack.
- **Secure Storage**: Credentials are saved in the OS-native secure storage (macOS Keychain, Windows Credential Manager, Linux Secret Service).
- **Certificate Enforcement**: We enforce the use of the IIITM CA Certificate to ensure you are connecting to the legitimate IIITM RADIUS server, protecting you from malicious "evil twin" hotspots.
- **Open and Auditable**: All configuration files (`.mobileconfig`, `.xml`, scripts) are open-source and can be inspected by anyone or the IT department.

## Reporting a Vulnerability

If you discover a security issue, please do not open a public issue. Instead, contact the maintainer **Ayush Sah** at [imt_2022026@iiitm.ac.in](mailto:imt_2022026@iiitm.ac.in).
