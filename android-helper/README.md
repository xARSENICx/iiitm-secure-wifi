# Android Helper App (Blueprint)

This directory contains the source code fragments for a lightweight Android APK that automates the Wi-Fi configuration using the `WifiNetworkSuggestion` API.

## Implementation Details

- **EAP Method**: TTLS
- **Phase 2**: PAP
- **CA Cert**: Embedded as a resource (`res/raw/iiitm_ca.crt`)
- **Domain**: `iiitm.ac.in`

## How to Build

1. Open Android Studio and create a new Project.
2. Use the package name `in.ac.iiitm.secure`.
3. Copy **`WifiOnboarder.kt`** into your source folder.
4. Place the **`IIITM-CA.crt`** into `app/src/main/res/raw/`.
5. Call `WifiOnboarder.onboard(this)` from a Button click listener in your `MainActivity`.

## User Experience

1. Student opens the app.
2. Clicks "Connect to IIITM Wi-Fi".
3. Android asks: "Allow IIITM Connect to suggest Wi-Fi networks?".
4. Student clicks **Allow**.
5. Done. They can now go to Wi-Fi settings and tap the network to connect.
