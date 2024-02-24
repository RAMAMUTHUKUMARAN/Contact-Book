import tkinter as tk
from tkinter import messagebox

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.contacts = []

        # Create and set up GUI components
        self.create_gui()

    def create_gui(self):
        # Labels
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry widgets
        self.name_entry = tk.Entry(self.root)
        self.phone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contact List", command=self.view_contact_list).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.destroy).grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contact_list(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
            return

        contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in self.contacts])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            for contact in self.contacts:
                if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                    messagebox.showinfo("Contact Found", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
                    return
            messagebox.showinfo("Contact Not Found", "No matching contact found.")

    def update_contact(self):
        search_query = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_query:
            for i, contact in enumerate(self.contacts):
                if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                    updated_name = simpledialog.askstring("Update Contact", "Enter updated name:", initialvalue=contact['Name'])
                    updated_phone = simpledialog.askstring("Update Contact", "Enter updated phone number:", initialvalue=contact['Phone'])
                    updated_email = simpledialog.askstring("Update Contact", "Enter updated email:", initialvalue=contact['Email'])
                    updated_address = simpledialog.askstring("Update Contact", "Enter updated address:", initialvalue=contact['Address'])

                    self.contacts[i] = {'Name': updated_name, 'Phone': updated_phone, 'Email': updated_email, 'Address': updated_address}
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    return
            messagebox.showinfo("Contact Not Found", "No matching contact found.")

    def delete_contact(self):
        search_query = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_query:
            for i, contact in enumerate(self.contacts):
                if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
                    confirmation = messagebox.askyesno("Delete Contact", f"Do you want to delete the contact:\nName: {contact['Name']}\nPhone: {contact['Phone']}")
                    if confirmation:
                        del self.contacts[i]
                        messagebox.showinfo("Success", "Contact deleted successfully!")
                        return
            messagebox.showinfo("Contact Not Found", "No matching contact found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()
