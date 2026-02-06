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

def install_wifi():
    os_name = platform.system()
    
    if os_name == "Darwin": # macOS
        print("[*] Detected macOS. Launching Configuration Profile...")
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "macos-ios", "IIITM_Secure_WiFi.mobileconfig"))
        if os.path.exists(config_path):
            subprocess.run(["open", config_path])
            print("\n[+] Configuration Profile Opened!")
            print("NEXT STEPS:")
            print("1. Open 'System Settings' (or System Preferences).")
            print("2. Look for a 'Profiles Downloaded' notification or go to Privacy & Security -> Profiles.")
            print("3. Double-click the 'IIITM Secure Wi-Fi' profile to install it.")
            print("4. Follow the on-screen prompts (enter your Mac password if asked).")
            print("5. Once installed, select the Wi-Fi network and log in with your LDAP credentials.")
            input("\nPress Enter once you have completed these steps...")
        else:
            print("[-] Error: Configuration profile not found.")
            
    elif os_name == "Linux":
        print("[*] Detected Linux. Applying NetworkManager configurations...")
        # Since Linux setup usually requires sudo, we check for it
        if os.geteuid() != 0:
            print("[!] This action requires root privileges. Please run with sudo.")
            return

        # Simple logic to copy .nmconnection files
        linux_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "linux"))
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
            print("\n[+] Wi-Fi Profiles Installed!")
            print("NEXT STEPS:")
            print("1. Open your system's Wi-Fi / Network menu.")
            print("2. Look for 'IIITM_Secure' or the relevant network name.")
            print("3. Click to connect.")
            print("4. If prompted, enter your LDAP Username and Password.")
            print("   - CA Certificate: No CA certificate is required (or select 'None' / 'Do not validate').")
            input("\nPress Enter once you have completed these steps...")
        else:
            print("[-] Error: No .nmconnection files found in linux directory.")

    elif os_name == "Windows":
        print("[*] Detected Windows.")
        install_bat = os.path.abspath(os.path.join(os.path.dirname(__file__), "windows", "install.bat"))
        if os.path.exists(install_bat):
            print("[*] Launching Windows Installer...")
            subprocess.run(["cmd", "/c", install_bat])
            print("\n[+] Installer script finished.")
            print("NEXT STEPS:")
            print("1. Check your Wi-Fi networks list.")
            print("2. Connect to the IIITM network.")
            print("3. Enter your LDAP credentials when prompted.")
            input("\nPress Enter once you have completed these steps...")
        else:
            print("[-] Error: install.bat not found.")
    else:
        print(f"[-] Unsupported OS: {os_name}")

def show_menu():
    print("\n[?] What would you like to do?")
    print("1. Setup Wi-Fi")
    print("2. Reset Password")
    print("3. Diagnose Issues (Doctor)")
    print("4. Exit")
    
    choice = input("\nSelect an option (1-4): ").strip()
    if choice == '1':
        install_wifi()
    elif choice == '2':
        reset_password()
    elif choice == '3':
        diagnose()
    elif choice == '4':
        sys.exit(0)
    else:
        print("[!] Invalid option. Please run the tool again.")

def setup_wifi():
    print_banner()

    try:
        first_time = input("Is this your first time using the tool? (y/n): ").strip().lower()
        if first_time in ['y', 'yes']:
            print("\n[*] Important: You must reset your password on the LDAP portal first.")
            print(f"[*] Link: {LDAP_URL}")
            
            check_done = input("Are you done with the password reset? (y/n): ").strip().lower()
            if check_done in ['y', 'yes']:
                install_wifi()
            else:
                print("\n[!] Please reset your password and try again.")
                return
        else:
            show_menu()

    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

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

def print_help():
    print(f"""
IIITM Secure Wi-Fi Onboarding Tool v{VERSION}
============================================

Usage: python3 iiitm-wifi.py [COMMAND]

Commands:
  setup    Start the interactive setup wizard (Default)
  reset    Open the LDAP password reset portal
  doctor   Run connectivity and hardware diagnostics
  version  Show version information
  help     Show this help message

Examples:
  python3 iiitm-wifi.py          # Interactive mode
  python3 iiitm-wifi.py doctor   # Run diagnostics directly
""")

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", nargs="?", default="setup", choices=["setup", "reset", "doctor", "version", "help"])

    try:
        args = parser.parse_args()
    except SystemExit:
        print_help()
        sys.exit(1)
    
    if args.command == "setup":
        setup_wifi()
    elif args.command == "reset":
        reset_password()
    elif args.command == "doctor":
        diagnose()
    elif args.command == "version":
        print(f"IIITM Wi-Fi CLI v{VERSION}")
    elif args.command == "help":
        print_help()

if __name__ == "__main__":
    main()
