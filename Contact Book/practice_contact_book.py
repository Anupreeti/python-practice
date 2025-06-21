# Add contact

# View all contacts

# Search contact by name

# Delete contact

contact={}

def add_contact():
    name = input("Enter name: ")
    phone = input("Eneter phone number: ")
    email = input("Enetr email: ")
    contact[name] = {"phone":phone,"email":email}
    print(contact)

def view_contact():
    if not contact:
        print("No contact found")
        return False
    for name,info in contact.items():
        print(f"{name}- Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact:
        print(f"Found - {name} - {contact[name]}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to Delete= ")
    if name in contact:
        del contact[name]
        print("Contact Deleted")
    else:
        print("Contact not found")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Enter your choice from 1-5: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid Choice")
