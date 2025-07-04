import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        return f"{self.name} - {self.phone}"

class ContactBookApp(Person):
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Phone").pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        tk.Label(self.root, text="Address").pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

        tk.Label(self.root, text="Search by Name or Phone").pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        tk.Button(self.root, text="Search", command=self.search_contact).pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.load_contact)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Person(name, phone, email, address)
            self.contacts.append(contact)
            self.update_listbox()
            self.clear_fields()
        else:
            messagebox.showwarning("Input Error", "Name and phone are required.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, contact.display())

    def load_contact(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)

            self.name_entry.insert(0, contact.name)
            self.phone_entry.insert(0, contact.phone)
            self.email_entry.insert(0, contact.email)
            self.address_entry.insert(0, contact.address)

    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                self.contacts[index] = Person(name, phone, email, address)
                self.update_listbox()
                self.clear_fields()
            else:
                messagebox.showwarning("Input Error", "Name and phone are required.")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.contacts[index]
            self.update_listbox()
            self.clear_fields()

    def search_contact(self):
        query = self.search_entry.get().lower()
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone:
                self.listbox.insert(tk.END, contact.display())

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
