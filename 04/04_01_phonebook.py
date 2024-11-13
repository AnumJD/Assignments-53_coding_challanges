"""Problem Statement: In this program we show an example of using dictionaries to keep track of information in a phonebook."""
#Solution 
def main():
    phonebook = {}
    
    def add_contact(name, number):
        phonebook[name] = number
        print(f"Contact {name} added with the number {number}")
        
    def get_contact(name):
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"Contact {name} is not found")
            
    def update_contact(name, number):
        if name in phonebook:
            phonebook[name] = number
            print(f"{name}'s number has been updated to {number}")
        else:
            print(f"Contact {name} not found. Please add the contact first.")
            
    def delete_contact(name):
        if name in phonebook:
            del phonebook[name]
            print(f"Contact {name} is deleted")
        else:
            print(f"Contact {name} is not found")
            
    def list_contacts():
        if phonebook:
            print("Phonebook Contacts:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Phonebook is empty")

    # Main loop to manage the phonebook
    while True:
        print("\nPhonebook Menu")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")
    
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            name = input("Enter the name: ")
            number = input("Enter Phone No: ")  # Allow any input format
            add_contact(name, number)

        elif choice == '2':
            name = input("Enter Name: ")
            get_contact(name)
    
        elif choice == '3':
            name = input("Enter Name: ")
            number = input("Enter Number: ")  # Allow any input format
            update_contact(name, number)
    
        elif choice == '4':
            name = input("Enter Name: ")
            delete_contact(name)
        
        elif choice == '5':
            list_contacts()
            
        elif choice == '6':
            print("Exiting the program")
            break
            
        else: 
            print("Invalid choice. Please choose from the menu between 1-6")


if __name__ == "__main__":
    main()