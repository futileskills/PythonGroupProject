# Basic script to keep track of inventory. Dumps scans into inventory.csv and allows search and editing
# Need to flush out search options. Break into sub menu? 
# Im fucking tired


#---------------SOURCES AND DOCS-------------------
# CSV import docs and "man page" 
#	https://python-adv-web-apps.readthedocs.io/en/latest/csv.html




import csv
import os

def load_inventory(filename):
    """Load inventory from a CSV file and return as a list of dictionaries."""
    inventory = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(row)
    return inventory

def save_inventory(filename, inventory):
    """Save inventory to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Barcode', 'Description', 'Price', 'Owner']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

def display_inventory(inventory):
    """Display the current inventory."""
    if inventory:
        print("Current Inventory:")
        for item in inventory:
            print(f"Barcode: {item['Barcode']}, Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")
    else:
        print("Inventory is empty.")

def add_item(inventory):
    """Add an item to the inventory with barcode validation."""
    while True:
        while True:
            barcode = input("Enter the barcode: ")
            if len(barcode) < 5:  # Example validation: barcode must be at least 5 characters
                print("Barcode is too short. Please enter a valid barcode.")
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

def edit_item(inventory):
    """Edit an item in the inventory based on the barcode."""
    barcode = input("Enter the barcode of the item to edit: ")
    for item in inventory:
        if item['Barcode'] == barcode:
            print("Current details:")
            print(f"Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")
            
            item['Description'] = input("Enter new description (leave blank to keep current): ") or item['Description']
            item['Price'] = input("Enter new price (leave blank to keep current): ") or item['Price']
            item['Owner'] = input("Enter new owner's name (leave blank to keep current): ") or item['Owner']
            print("Item updated.")
            return
    print("Item not found.")

def search_item(inventory):
    """Search for an item by barcode."""
    barcode = input("Enter the barcode to search: ")
    for item in inventory:
        if item['Barcode'] == barcode:
            print(f"Found item - Barcode: {item['Barcode']}, Description: {item['Description']}, Price: {item['Price']}, Owner: {item['Owner']}")
            return
    print("Item not found.")

def main_menu():
    """Display the main menu and handle user choices."""
    filename = 'inventory.csv'
    inventory = load_inventory(filename)

    while True:
        print("\nMain Menu:")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Edit Item")
        print("4. Search Item")
        print("5. Save and Exit")
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
            save_inventory(filename, inventory)
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
