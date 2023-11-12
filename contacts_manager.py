import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def search_contact(self, keyword):
        keyword = keyword.lower()
        return [contact for contact in self.contacts if keyword in contact.name.lower()]

class AddressBookApp:
    def __init__(self, root):
        self.address_book = AddressBook()

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.name_label = ttk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        self.phone_label = ttk.Label(self.frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w")

        self.phone_entry = ttk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1, padx=5)

        self.email_label = ttk.Label(self.frame, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")

        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=5)

        self.add_button = ttk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, pady=10)

        self.search_label = ttk.Label(self.frame, text="Search by Name:")
        self.search_label.grid(row=4, column=0, sticky="w")

        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=4, column=1, padx=5)

        self.search_button = ttk.Button(self.frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=4, column=2, pady=10)

        self.contacts_listbox = tk.Listbox(self.frame, height=10)
        self.contacts_listbox.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.address_book.add_contact(name, phone, email)
            self.update_contacts_list()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Incomplete Information", "Please enter all contact details.")

    def search_contact(self):
        keyword = self.search_entry.get()
        if keyword:
            search_results = self.address_book.search_contact(keyword)
            self.display_search_results(search_results)
        else:
            self.update_contacts_list()

    def display_search_results(self, results):
        self.contacts_listbox.delete(0, tk.END)
        for contact in results:
            self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone} - {contact.email}")

    def update_contacts_list(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.address_book.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone} - {contact.email}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Address Book")
    app = AddressBookApp(root)
    root.mainloop()
