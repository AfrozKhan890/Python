# Contact Book Project
Contacts = []

def Add_Contact(Name,Phone_Number):
    Contacts.append({"Name": Name, "Phone Number": Phone_Number})    
    print(f"Contact {Name} added successfully.")
    
def Search_Contact(Name):
    for Contact in Contacts:
        if Contact["Name"].lower() == Name.lower():
            print(f"This Contact is Found: \nName: {Contact['Name']}, \nPhone Number: {Contact['Phone Number']}")
            return
    print(f"Contact {Name} not found.")
    
    
def Delete_Contact(Name):
    for Contact in Contacts:
        if Contact["Name"].lower()  == Name.lower():
            Contacts.remove(Contact)
            print(f"Contact {Name} deleted successfully.")
            return
    print(f"Contact {Name} not found.")

def Display_Contacts():
    if not Contacts:
        print("No Contacts found.")
    else:
        for Contact in Contacts:
            print(f"Name: {Contact['Name']}, Phone Number: {Contact['Phone Number']}")




# Main Program Loop
while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        Name = input("Enter contact name: ")
        Phone_Number = input("Enter phone number: ")
        Add_Contact(Name, Phone_Number)
    
    elif choice == '2':
        Name = input("Enter the name to search: ")
        Search_Contact(Name)
    
    elif choice == '3':
        Name = input("Enter the name to delete: ")
        Delete_Contact(Name)
    
    elif choice == '4':
        Display_Contacts()
    
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
