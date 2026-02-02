#!/usr/bin/env python3
import sys
import os
import subprocess
import platform
import webbrowser
import argparse

VERSION = "1.0.0"
LDAP_URL = "https://ldap.iiitm.ac.in"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
    =========================================
    IIITM Secure Wi-Fi Onboarding - v{VERSION}
    =========================================
    Community Maintained - Unofficial Tool
    """
    print(banner)

def setup_wifi():
    print_banner()
    os_name = platform.system()
    
    if os_name == "Darwin": # macOS
        print("[*] Detected macOS. Launching Configuration Profile...")
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "macos-ios", "IIITM_Secure_WiFi.mobileconfig"))
        if os.path.exists(config_path):
            subprocess.run(["open", config_path])
            print("[+] Success: Profile opened. Please follow the prompt in 'System Settings' to finish installation.")
        else:
            print("[-] Error: Configuration profile not found.")
            
    elif os_name == "Linux":
        print("[*] Detected Linux. Applying NetworkManager configurations...")
        # Since Linux setup usually requires sudo, we check for it
        if os.geteuid() != 0:
            print("[!] This action requires root privileges. Please run with sudo.")
            return

        # Simple logic to copy .nmconnection files
        linux_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "linux"))
        nm_path = "/etc/NetworkManager/system-connections/"
        
        found = False
        for f in os.listdir(linux_dir):
            if f.endswith(".nmconnection"):
                src = os.path.join(linux_dir, f)
                dst = os.path.join(nm_path, f)
                print(f"[*] Installing profile: {f}")
                subprocess.run(["cp", src, dst])
                subprocess.run(["chmod", "600", dst])
                found = True
        
        if found:
            print("[*] Reloading NetworkManager...")
            subprocess.run(["nmcli", "connection", "reload"])
            print("[+] Success: Wi-Fi profiles installed. You can now connect via your network menu.")
        else:
            print("[-] Error: No .nmconnection files found in linux directory.")

    elif os_name == "Windows":
        print("[*] Detected Windows.")
        install_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "windows", "install.bat"))
        if os.path.exists(install_bat):
            print("[*] Launching Windows Installer...")
            subprocess.run(["cmd", "/c", install_bat])
        else:
            print("[-] Error: install.bat not found.")
    else:
        print(f"[-] Unsupported OS: {os_name}")

def reset_password():
    print("[*] Opening IIITM LDAP Password Portal...")
    webbrowser.open(LDAP_URL)
    print(f"[+] If it doesn't open, visit: {LDAP_URL}")
    print("[!] Note: This link only works when connected to the IIITM internal network.")

def diagnose():
    print_banner()
    print("[*] Running Diagnostics...")
    
    # Check LDAP connectivity
    print("[*] Checking LDAP Server reachability...")
    try:
        # Use a quick ping or curl check
        res = subprocess.run(["ping", "-c", "1", "-W", "2", "ldap.iiitm.ac.in"], capture_output=True)
        if res.returncode == 0:
            print("[+] LDAP Server is REACHABLE.")
        else:
            print("[-] LDAP Server is UNREACHABLE. (Are you on IIITM Network?)")
    except:
        print("[-] Could not run ping.")

    # Check WiFi adapter status
    print("[*] Checking Wi-Fi Hardware...")
    if platform.system() == "Darwin":
        subprocess.run(["networksetup", "-getairportpower", "en0"])
    elif platform.system() == "Linux":
        subprocess.run(["nmcli", "radio", "wifi"])

def main():
    parser = argparse.ArgumentParser(description="IIITM Secure Wi-Fi Management Tool")
    parser.add_argument("command", choices=["setup", "reset", "doctor", "version"], help="Action to perform")
    
    args = parser.parse_args()
    
    if args.command == "setup":
        setup_wifi()
    elif args.command == "reset":
        reset_password()
    elif args.command == "doctor":
        diagnose()
    elif args.command == "version":
        print(f"IIITM Wi-Fi CLI v{VERSION}")

if __name__ == "__main__":
    main()
