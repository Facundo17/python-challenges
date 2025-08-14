"""
Build a command-line app that allows a small business to manage their inventory. The app will let users:

add new items to the inventory,
view current inventory,
update item quantities,
search for an specific item.

NOTE: check the reference folder for more details.
"""

stock = {}

def check_inventory():
    """Check if the inventory is empty."""
    if not stock or stock == {}:
        print("Inventory is empty.")
        return False
    return True

def add_item():
    """Add a new item to the inventory."""
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    if item_name in stock:
        print(f"{item_name} already exists in inventory. Use update option to change quantity.")
    else:
        stock[item_name] = { 'quantity': quantity, 'price': price }
        print(f"Item added successfully!")

def update_stock():
    """Update the quantity of an existing item in the inventory."""
    if not check_inventory():
        return
    
    item_name = input("Enter item name to update: ")
    if item_name in stock:
        quantity = int(input("Enter new quantity: "))
        stock[item_name]['quantity'] = quantity
        print(f"Stock updated successfully")
    else:
        print(f"{item_name} does not exist in inventory.")

def view_inventory():
    """Display the current inventory."""
    if not check_inventory():
        return
    
    print("\nInventory:")
    i = 0
    for item, details in stock.items():
        i += 1
        print(f"{i}. {item}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def search_item():
    """Search for a specific item in the inventory."""
    if not check_inventory():
        return
    
    item_name = input("Enter item name to search: ")
    if item_name in stock:
        details = stock[item_name]
        print(f"Found: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
    else:
        print(f"{item_name} not found in inventory.")

while True:
    print("\nInventory Management System")
    print("1. Add New Item")
    print("2. Update Stock")
    print("3. View Inventory")
    print("4. Search for an Item")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_stock()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
         search_item()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")