# Add a contact (name, phone, email)
# View all contacts
# Search contact by name
# Delete a contact
# Store everything in contacts.json

import json
import argparse
from datetime import datetime
import os
import shutil

def load_file():
    try:
        with open("contacts.json", "r+") as f:
            return json.load(f)
    except Exception as e:
        return []

def save_file(contacts):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"contacts_backup_{timestamp}.json"
    if os.path.exists("contacts.json"):
        shutil.copy("contacts.json", backup_file)
    with open("contacts.json","w") as f:
        contact_list = sorted(contacts, key=lambda x: x['name'])
        json.dump(contact_list, f, indent =2)


def add_contact(name, phone, email):
    contacts = load_file()
    data = {"name":name, "phone": phone, "email": email}
    contacts.append(data)
    save_file(contacts)
    print("Contact Added")

def view_contacts():
    contacts = load_file()
    if not contacts:
        print("There is no contact in the file")
    else:
        for contact in contacts:
            print(contact)

def search_contact(name):
    contacts = load_file()
    item = [contact for contact in contacts if contact['name'] == name]
    if item:
        print(item)
    else:
        print("Contact not found")

def delete_contact(name):
    contacts = load_file()
    found = [contact for contact in contacts if contact['name'] == name]
    if found:
        contact = [item for item in contacts if item['name'] !=name]
        save_file(contact)
        print("Contact deleted")
    else:
        print("Contact not found")

def update_contact(name, phone, email):
    contacts = load_file()
    # contact_list = [contact for contact in contacts if contact['name'] == name]
    for contact in contacts:
        if contact['name'] == name:
            contact['email'] = email
            contact['phone'] = phone
        else:
            print("Contact not found")
            break
    save_file(contacts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("choice", choices=["1","2","3","4","5"], help="Enter your choice 1.Add contact 2.View all Contacts 3.Search Contact 4.Delete Contact 5.Update contact")
    parser.add_argument("--name", help="Enter Contact Name")
    parser.add_argument("--phone", help="Enter phone Number")
    parser.add_argument("--email", help="Enter email")
    args=parser.parse_args()

    if args.choice == "1":
        if args.name and args.phone and args.email:
            add_contact(args.name, args.phone, args.email)
        else:
            print("Please mentione the contact details to be addedd")
    elif args.choice == "2":
        view_contacts()
    elif args.choice == "3":
        if args.name:
            search_contact(args.name)
        else:
            print("Please provide the name of the contact you are trying to search")
    elif args.choice == "4":
        if args.name:
            delete_contact(args.name)
        else:
            print("Please share the contact name to be deleted")
    elif args.choice == "5":
        if args.name and args.email and args.phone:
            update_contact(args.name, args.phone, args.email)
        else:
            print("Please provide valid detaisl for contact to be updated")
