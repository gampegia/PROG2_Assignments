"""
Prog 2
W03
P02 1.2 Bank application

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 11.03.2024
"""

from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from YouthAccount import YouthAccount
import datetime 
import time


# The BankApplication class is the main
class BankApplication:
    def __init__(self):
        self.accounts = []
        self.current_account = None

    # Method to open a new account
    def open_account(self, account_type):
        owner = input("Enter the owner's name: ")
        account_type = account_type.lower()

        # Create an instance of the appropriate account type
        if account_type == "savings":
            account = SavingsAccount(owner)

        elif account_type == "youth":
            # Ask for the date of birth and create a YouthAccount instance
            try:
                date_of_birth = input("Enter the date of birth (dd-mm-yyyy): ")
                
                account = YouthAccount(owner, date_of_birth)

            except ValueError:
                print("Invalid date of birth")
                return

        else:
            print("Invalid account type")
            return
        
        # Add the account to the list of accounts
        self.accounts.append(account)
        print(f"{account_type.capitalize()} account opened successfully")
        print("Account number: ", account.account_number)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed successfully")
                return

        print(f"Account {account_number} not found")

    def check_balance(self, account_number):
        for account in self.accounts:
            if str(account.account_number) == str(account_number):
                print(f"Account {account_number} has a balance of {account.balance} {account.currency}")
                return

            print(f"Account {account_number} not found")


    # Method to display the menu
    def display_menu(self):
        print("1. Open account")
        print("2. Close account")
        print("3. Check balance")
        print("4. Exit")
       
 
    # Method to run the application
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                account_type = input("Enter account type (savings/youth): ")
                self.open_account(account_type)
            elif choice == "2":
                account_number = input("Enter account number: ")
                self.close_account(account_number)

            elif choice == "3":
                account_number = input("Enter account number: ")
                self.check_balance(account_number)

            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

# Instantiate the BankApplication class and run the application
if __name__ == "__main__":
    bank_app = BankApplication()
    bank_app.run()