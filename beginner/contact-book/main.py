import re

contacts=[]
# Add a new contact
def add_contact(contacts):
    print("Please add a contact:")
    while True:
        name = input("Name: ").strip()
        if not name:
            print("Name can not be Empty!")
            continue
        break

    while True:
        phone = input("Phone: ").strip()
        if not phone:
            print("Phone can not be Empty!")
            continue
        if len(phone)!=11:
            print("Phone number must be 11 digits")
            continue
        if not phone.isdigit():
            print("Phone number must contain only digits.")
            continue
        if not phone.startswith("09"):
            print("Phone number must start with 09")
            continue
        break

    while True:
        email=input("Email: ").strip()
        pattern= r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not email:
            print("Email can not be Empty!")
            continue
        if re.fullmatch(pattern,email) is None:
            print("Email is not Valid!")
            continue

        break
    contacts.append(
        {
            "name":name,
            "phone":phone,
            "email":email
        }
    )
    print("Contact successfully added!")

# Display all contacts
def show_contacts(contacts):
    if not contacts:
        print("The list is empty! Add a contact, then try again.")
    else:
        for index,contact in enumerate(contacts,start=1):
            print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search for a contact
def search_contact(contacts,searched_contact):
    for contact in contacts:
        if contact['name'].lower() == searched_contact.lower():
            print(f"Result: {contact['name']} | {contact['phone']} | {contact['email']} ")
            break
    else:
        print("Contact not found")

# Delete a contact
def delete_contact(contacts):
    if not contacts:
        print("The list is empty! Add a contact, then try again.")
        return
    contact_name=input("Please enter a name you want to delete :").strip()
    for index, contact in enumerate(contacts):
        if contact['name'].lower() == contact_name.lower():
            contacts.pop(index)
            print(f"{contact['name']} deleted!")
            break
    else:
        print("Contact not found")

# Main program loop
while True:

    print("""===== CONTACT BOOK =====
1. Add contact
2. Show contacts
3. Search contact
4. Delete contact
5. Exit""")
    print()
    option=input("Choose a number:")
    if option=="1":
        add_contact(contacts)

    elif option=="2":
        show_contacts(contacts)

    elif option=="3":
        searched_contact = input("Please search your contact name: ").strip()
        search_contact(contacts, searched_contact)

    elif option=="4":
        delete_contact(contacts)

    elif option=="5":
        print("Goodbye...")
        break

    else:
        print("You must enter a number between 1-5")
