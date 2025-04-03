# TODO: Import Budget and Transaction classes

def main():
    budget = Budget()
    budget.load_from_file("budget_data.txt")

    while True:
        print("\n1. Add Transaction\n2. View Summary\n3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # TODO: Get input and create Transaction
            # TODO: Add transaction to budget
            pass

        elif choice == "2":
            # TODO: Print each transaction
            # TODO: Print current balance
            pass

        elif choice == "3":
            budget.save_to_file("budget_data.txt")
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
