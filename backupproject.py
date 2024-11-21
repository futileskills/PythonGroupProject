# Basic script to keep track of inventory. Dumps scans into inventory.csv and allows search and editing
# Need to flush out search options. Break into sub menu?
# Need to add checking for reused barcodes. throw error and loop to try again
# If yall have any questions just add it here or in the questions.txt file. Ill get the notification


#---------------SOURCES AND DOCS-------------------
# CSV import docs and "man page"
#	https://python-adv-web-apps.readthedocs.io/en/latest/csv.html


#---------- TODO LIST ----------
# Need to add a way to add lines or columns to the csv file without it breaking.
# Is there a way to just edit the csv file directly without this program having a bitch fit for new columns.
# Need to add a way to append the csv file when editing 


import csv
import os


def load_inventory(filename):
    # Load inventory from a CSV file and return a list
    inventory = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(row)
    return inventory


def save_inventory(filename, inventory):
    # Save inventory to a CSV file
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Barcode', 'Description', 'Price', 'Owner']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)


def display_inventory(inventory):
    # Display the current inventory.
    if inventory:
        print("Current Inventory:")
        for item in inventory:
            print(f"Barcode: {item['Barcode']}, Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")
    else:
        print("Inventory is empty.")


def add_item(inventory):
    # Add an item to inventory & barcode verification
    while True:
        while True:
            barcode = input("Enter the barcode: ")
            if len(barcode) < 5:  # Barcode must be at least 5 characters
                print("Barcode is too short. Must be at least 5 characters long.")
                continue

            # Check if barcode exists
            if barcode_exists(inventory, barcode):
                print("Barcode already used in database.")
                continue

            # Confirm barcode
            confirm = input(f"You entered barcode '{barcode}'. Is this correct? (y/n): ").lower()
            if confirm == 'y':
                break  # Exit the inner loop if barcode is confirmed
            else:
                print("Let's try again.")

        description = input("Enter the description: ")
        price = input("Enter the price: ")
        owner = input("Enter the owner's name: ")

        inventory.append({'Barcode': barcode, 'Description': description, 'Price': price, 'Owner': owner})

        if input("Add another item? (y/n): ").lower() != 'y':
            break


def search_item(inventory):
    """Search for an item by barcode."""
    barcode = input("Enter the barcode to search: ")
    for item in inventory:
        if item['Barcode'] == barcode:
            print(f"Found item - Barcode: {item['Barcode']}, Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")
            return
    print("Item not found.")


def edit_item(inventory):
    # Edit an item in the inventory based on the barcode
    barcode = input("Enter the barcode of the item to edit: ")
    for item in inventory:
        if item['Barcode'] == barcode:
            print("Current details:")
            print(f"Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")

            description = input("Enter new description (leave blank to keep current): ")
            price_input = input("Enter new price (leave blank to keep current): ")
            owner = input("Enter new owner's name (leave blank to keep current): ")

            # Ensure the barcode is still unique
            while True:
                new_barcode = input(f"Enter new barcode (leave blank to keep current: {barcode}): ")
                if not new_barcode:
                    new_barcode = barcode  # Keep the current barcode if the user leaves it blank
                if new_barcode != barcode and barcode_exists(inventory, new_barcode, exclude_barcode=barcode):
                    print("Barcode already exists. Please enter a unique barcode.")
                    continue
                break

            # Apply changes
            item['Barcode'] = new_barcode
            item['Description'] = description or item['Description']
            item['Price'] = float(price_input) if price_input else item['Price']
            item['Owner'] = owner or item['Owner']

            print("Item updated.")
            return
    print("Item not found.")


def delete_item(inventory):
    # Delete an item from inventory based on barcode
    barcode = input("Enter the barcode of the item to delete: ")
    for item in inventory:
        if item['Barcode'] == barcode:
            inventory.remove(item)  # Remove from inventory
            print(f"Item with barcode {barcode} deleted.")
            save_inventory('inventory.csv', inventory)  # Save the updated inventory back to the CSV
            return
    print("Item not found.")


# Barcode existence check function
def barcode_exists(inventory, barcode, exclude_barcode=None):
    for item in inventory:
        if item['Barcode'] == barcode and barcode != exclude_barcode:
            return True
    return False


def main_menu():
    # Display the main menu
    filename = 'inventory.csv'
    inventory = load_inventory(filename)

    # Display the "Main Menu" ASCII art manually
    print("""
 __  __    _    ___ _   _   __  __ _____ _   _ _   _ 
|  \/  |  / \  |_ _| \ | | |  \/  | ____| \ | | | | |
| |\/| | / _ \  | ||  \| | | |\/| |  _| |  \| | | | |
| |  | |/ ___ \ | || |\  | | |  | | |___| |\  | |_| |
|_|  |_/_/   \_\___|_| \_| |_|  |_|_____|_| \_|\___/ 
    """)

    while True:
        print("\nMain Menu:")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Edit Item")
        print("4. Search Item")
        print("5. Delete Item")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            edit_item(inventory)
        elif choice == '4':
            search_item(inventory)
        elif choice == '5':
            delete_item(inventory)
        elif choice == '6':
            save_inventory(filename, inventory)
            print("Inventory saved. Exiting.")
            print("""
              ____  ___   ___  ____  ______   _______ 
             / ___|/ _ \ / _ \|  _ \| __ ) \ / / ____|
            | |  _| | | | | | | | | |  _  \\ V /|  _|  
            | |_| | |_| | |_| | |_| | |_) || | | |___ 
             \____|\___/ \___/|____/|____/ |_| |_____|
            """)

            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
