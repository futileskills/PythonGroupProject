# start of group project
# Writing a program to detect OS, print off System info, dump wireless info, and local ip info



import os
import platform
import subprocess
import re

def check_os():
    return platform.system()

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()  # Strip whitespace for cleaner output
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None

def dump_wireless_passwords():
    os_type = check_os()
    if os_type == 'Linux':
        print("Wireless password dumping is typically not straightforward on Linux.")
        print("Here, we show saved Wi-Fi configurations:")
        output = run_command("sudo grep -r '^psk=' /etc/NetworkManager/system-connections/")
        if output:
            print(output)
        else:
            print("No wireless passwords found or command failed.")
    elif os_type == 'Windows':
        profiles_output = run_command("netsh wlan show profiles")
        if profiles_output:
            profiles = re.findall(r"All User Profile\s+:\s+(.*)", profiles_output)
            for profile in profiles:
                ssid = profile.strip()
                password_output = run_command(f"netsh wlan show profile \"{ssid}\" key=clear")
                if password_output:
                    password = re.search(r"Key Content\s+:\s+(.*)", password_output)
                    if password:
                        print(f"SSID: {ssid}, Password: {password.group(1)}")
                    else:
                        print(f"SSID: {ssid}, Password: Not found or not set.")
        else:
            print("No Wi-Fi profiles found or command failed.")
    else:
        print("Unsupported OS for dumping wireless passwords.")

def main():
    os_type = check_os()
    print(f"Detected OS: {os_type}")
    
    while True:
        print("\nMenu:")
        print("1. Show IP address (Linux: ip addr / Windows: ipconfig)")
        print("2. Show OS information (uname or ver)")
        print("3. Dump Wireless Passwords")
        print("4. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
            if os_type == 'Linux':
                output = run_command("ip addr")
                print(output if output else "No output for 'ip addr' command.")
            elif os_type == 'Windows':
                output = run_command("ipconfig")
                print(output if output else "No output for 'ipconfig' command.")
            else:
                print("Unsupported OS.")
        elif choice == '2':
            if os_type == 'Linux':
                output = run_command("uname -a")
                print(output if output else "No output for 'uname' command.")
            elif os_type == 'Windows':
                output = run_command("ver")
                print(output if output else "No output for 'ver' command.")
            else:
                print("Unsupported OS.")
        elif choice == '3':
            dump_wireless_passwords()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

