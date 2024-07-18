class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. {contact}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(f"Found Contact:\n{contact}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        contact_index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= contact_index < len(self.contacts):
            contact = self.contacts[contact_index]
            print(f"\nCurrent Contact:\n{contact}")
            name = input(f"Enter new name (leave blank to keep '{contact.name}'): ")
            phone_number = input(f"Enter new phone number (leave blank to keep '{contact.phone_number}'): ")
            email = input(f"Enter new email (leave blank to keep '{contact.email}'): ")
            address = input(f"Enter new address (leave blank to keep '{contact.address}'): ")
            contact.name = name or contact.name
            contact.phone_number = phone_number or contact.phone_number
            contact.email = email or contact.email
            contact.address = address or contact.address
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_index < len(self.contacts):
            del self.contacts[contact_index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()