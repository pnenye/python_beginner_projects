# TODO: Import ContactManager and Contact classes

def main():
    manager = ContactManager()
    manager.load_from_file("contacts.txt")

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search\n4. Delete\n5. Save & Exit")
        choice = input("Option: ")

        if choice == "1":
            # TODO: Get input and add contact
            pass

        elif choice == "2":
            # TODO: Print all contacts
            pass

        elif choice == "3":
            # TODO: Search contacts
            pass

        elif choice == "4":
            # TODO: Delete contact
            pass

        elif choice == "5":
            manager.save_to_file("contacts.txt")
            print("Saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
