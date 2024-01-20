import json
import os

def load_contacts(filename='contacts.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")

    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    for name, info in contacts.items():
        print(f"\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")

def search_contacts(contacts):
    search_term = input("Enter a name to search for: ")
    if search_term in contacts:
        contact = contacts[search_term]
        print(f"\nName: {search_term}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        action = input("\nChoose an action - Add (A), View (V), Search (S), Exit (E): ").upper()

        if action == 'A':
            add_contact(contacts)

        elif action == 'V':
            view_contacts(contacts)

        elif action == 'S':
            search_contacts(contacts)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
