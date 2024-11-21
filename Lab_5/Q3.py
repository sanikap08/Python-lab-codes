# Define the BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        """Constructor to initialize the balance."""
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        """Method to check the current balance."""
        print(f"Current balance: {self.balance}")

# Create an object of the BankAccount class
account = BankAccount()

# Perform some transactions
account.deposit(500)
account.withdraw(200)
account.check_balance()
