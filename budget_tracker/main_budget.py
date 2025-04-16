# TODO: Import Budget and Transaction classes
from budget import Budget
from transaction import Transaction

def main():
    budget = Budget()
    #budget.load_from_file("budget_data.txt")

    while True:
        print("\n1. Add Transaction\n2. View Summary\n3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter Description: ")
            amount = int(input("Enter Amount: "))
            category = input("Enter Category: ")
            is_income = input("Enter income_description ?  Y/N:  ")
            
            # # TODO: Get input and create Transaction
            if is_income == "Y":
                    is_income = True
            else:
                is_income = False
            transaction = Transaction(description, amount, category, is_income)
            
            # TODO: Add transaction to budget
            budget.add_transaction(transaction)
      
        elif choice == "2":
            budget.get_balance()
              # TODO: Print current balance
            
            # TODO: Print each transaction
            transactions= budget.transaction
            for transaction in transactions:
                print(transaction)

        elif choice == "3":
            budget.save_to_file("budget_data.txt")
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
