#Lab Assignment -  Dictionaries Lab
#By: Brian Duke
#Date: 4/09/2025
#This program - This system will allow the user to manage contact information, including adding, searching, updating, and deleting contact details.

def add_contact(contacts):
    name = input("Enter Contact's Name: ")
    phone = input("Enter Contact's Phone Nnumber: ")
    email = input("Enter Contact's Email Address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact Added Successfully!")
    
def search_contact(contacts):
    name = input("Enter Contact Name: ")
    if name in contacts:
        print(f"Contact Found")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact Not Found.")
        
def update_contact(contacts):
    name = input("Enter Old Contact Name: ")
    if name in contacts:
        phone = input(f"Enter New Phone Number: {contacts[name]['phone']}")
        email = input(f"Enter New Email Address: {contacts[name]['email']}")
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found.")
        
def delete_contact(contacts):
    name = input("Enter Contact's Name: ")
    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found.")
    
def display_contacts(contacts):
    if not contacts:
        print("No Contacts Available")
        return
    print("Contacts:")
    for name, details in contacts.items():
        print(f"  Name: {name}")
        print(f"    Phone: {details['phone']}")
        print(f"    Email: {details['email']}")

def main():
    contacts = {}
    while True:
        print("\n--------- Menu: ---------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")
        print("-------------------------")

        menu = input("Enter 1-6: ")
        
        if menu == '1':
            add_contact(contacts)
        elif menu == '2':
            search_contact(contacts)
        elif menu == '3':
            update_contact(contacts)
        elif menu == '4':
            delete_contact(contacts)
        elif menu == '5':
            display_contacts(contacts)
        elif menu == '6':
            print("Have a Good Day!")
            break
        else:
            print("ERROR: PLEASE ONLY PUT 1-6")
    
if __name__ == "__main__":
    main()