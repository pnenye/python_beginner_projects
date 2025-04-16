# TODO: Import Transaction class from transaction.py
from transaction import Transaction

class Budget:
    def __init__(self):
        self.transaction = []
        # TODO: Create a list to store transactions

    def add_transaction(self, transaction):
        self.transaction.append(transaction)
        #TODO: Append the transaction to the list
        
# TODO: Loop through transactions and calculate the balance
    def get_balance(self):
        balance = 0
        for transaction in self.transaction:
            if transaction.is_income:
                balance +=transaction.amount
            else:
                balance -=transaction.amount
        return balance
    
    
    # TODO: Write transactions to a file
    def save_to_file(self,filename):
        with open(filename, "w") as file:
            for transaction in self.transaction:
                file.write(str(transaction))
                file.write("\n")

     # TODO: Read file and load transactions using Transaction class
     
    def load_from_file(self, filename):
        with open(filename, "r") as file:
            transactions_with_newline = file.readlines()
            for transaction in transactions_with_newline:
                transaction_without_newline = transaction[:-1]
                transaction_bits = transaction_without_newline.split("|")
                
                is_income_and_description = transaction_bits[0].strip()
                amount = transaction_bits[1].strip()
                category = transaction_bits[2].strip()
                
                #Get is_income and description details from "Income: Freelance"
                is_income_and_description = is_income_and_description.split(":")
                is_income = True if is_income == "Income" else False
                description = description.strip()
                
                #Get the amount details from "£500"
                amount = int(amount[1:])
                
                #Get the categort details from "Category: Work"
                category = category.split(":")[1].strip()
                
                transaction = Transaction(description,amount,category,is_income)
                
                self.transactions.append(transaction)
            