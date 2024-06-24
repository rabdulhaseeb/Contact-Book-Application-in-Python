contacts = []

def addContact():
    name = input("Name: ")
    number = input("Number: ")
    address = input("Address: ")
    relation = input("Relation: ")
    
    contact = {
       "Name": name,
       "Number": number,
       "Address": address,
       "Relation": relation 
    }
    
    contacts.append(contact)
    print("Contact added successfully!")
    
def removeContact():
    name = input("Enter the name of the contact to remove: ")
    for contact in contacts:
        if contact["Name"] == name:
            contacts.remove(contact)
            print(f"Contact {name} removed successfully!")
            return
    print(f"Contact {name} not found.")

def editContact():
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact["Name"] == name:
            number = input("New Number: ")
            address = input("New Address: ")
            relation = input("New Relation: ")
            
            contact["Number"] = number
            contact["Address"] = address
            contact["Relation"] = relation
            
            print(f"Contact {name} updated successfully!")
            return
    print(f"Contact {name} not found.")

def main():
    while True:
        print("""
        Contact Book
        Options: 
        1. Add Contact
        2. Remove Contact
        3. Edit Contact
        4. Show Contacts
        5. Exit
        """)
        
        option = input("Choose an option: ")
        
        if option == "1":
            addContact()
        elif option == "2":
            removeContact()
        elif option == "3":
            editContact()
        elif option == "4":
            for contact in contacts:
                print(contact)
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
