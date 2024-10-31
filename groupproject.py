# Writing pending. need to change a bunch of things -Mike

# Simple OS Info and Wi-Fi Password Dump Script

import os
import platform

def check_os():
    return platform.system()

def show_ip():
    
    os_type = check_os()
    if os_type == 'Linux':
        os.system("ip addr")
    elif os_type == 'Windows':
        os.system("ipconfig")
    else:
        print("Unsupported OS.")

def dump_wifi_passwords():
    
    if os_type == 'Linux':
        print("Showing saved Wi-Fi configurations (requires sudo):")
        os.system("sudo grep -r '^psk=' /etc/NetworkManager/system-connections/")
    elif os_type == 'Windows':
        print("Showing Wi-Fi profiles and passwords:")
        os.system("netsh wlan show profiles")
    else:
        print("Unsupported OS for dumping wireless passwords.")

def show_os_info():
    os_type = check_os()
    if os_type == 'Linux':
        os.system("uname -a")
    elif os_type == 'Windows':
        os.system("ver")
    else:
        print("Unsupported OS.")

def main():
    
    os_type = check_os()
    print(f"Detected OS: {os_type}")

    while True:
        print("\nMenu:")
        print("1. Show IP address")
        print("2. Show OS information")
        print("3. Dump Wi-Fi Passwords")
        print("4. Run All")
        print("5. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
            show_ip()
        elif choice == '2':
            show_os_info()
        elif choice == '3':
            dump_wifi_passwords()
        elif choice == '4':
            show_ip()
            show_os_info()
            dump_wifi_passwords()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

