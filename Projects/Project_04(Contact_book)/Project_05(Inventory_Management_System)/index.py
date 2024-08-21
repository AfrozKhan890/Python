# Inventory Management System

inventory = []


def display_inventory():
    if not inventory:
        print("The inventory is empty.\n")
    else:
        print("\n\nCurrent inventory: ")
        for item in inventory:
            print(f"Item Name: {item['name']}, Quantity: {item['quantity']}\n")
    print()


def add_item(name,quantity):
    for item in inventory:
        if(item["name"]) == name:
            print(f"{name} is already exist in inventory.Use update to change the quantity.\n")
            return
    inventory.append({'name': name, 'quantity': quantity})
    print(f"{name} is added to inventory with quantity {quantity}.\n")


def update_item(name,quantity):
    for item in inventory:
        if item['name'] == name:
            item['quantity'] = quantity
        print(f"{name} update with new quantity {quantity}.\n")
        return
    print(f"{name} not found in inventory.\n")
            
def remove_item(name):
    for item in inventory:
        if(item['name'] == name):
            inventory.remove(item)
            print(f"{name} removed from inventory.\n")
            return
    print(f"{name} is not found in inventory.\n")

def search_item(name):
    for item in inventory:
        if(item['name'] == name):
            print(f"{name}, Quantity: {item['quantity']}")
            return
    print(f"{name} is not found in inventory.\n")           
    

while True:
    print("Inventory Management System")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Search Item")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        display_inventory()
        
    elif choice == '2':
        name = input("Enter the item name: ")
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("The quantity is always positive.")
            else:
                add_item(name,quantity)
        except ValueError:
            print("Invalid input. Quantity must be integer.")
            
    elif choice == '3':
        name = input("Enter the item name: ")
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("The quantity is always positive.")
            else:
                update_item(name,quantity)
        except ValueError:
            print("Invalid input. Quantity must be integer.")
            
    elif choice == '4':
        name = input("Enter the item name: ")
        remove_item(name)
        
    elif choice == '5':
        name = input("Enter the item name: ")
        search_item(name)
        
    elif choice == '6':
        print("Exiting Inventory Management System")
        break
    else:
        print("Invalid choice. Please enter a number between 1 to 6.")
        


