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

class BankApplication:
    def __init__(self):
        self.accounts = []
        self.current_account = None

    def open_account(self, account_type):
        if account_type == "savings":
            account = SavingsAccount()
        elif account_type == "youth":
            account = YouthAccount()
        else:
            print("Invalid account type")
            return

        self.accounts.append(account)
        print(f"{account_type.capitalize()} account opened successfully")

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed successfully")
                return

        print(f"Account {account_number} not found")

    def select_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.current_account = account
                print(f"Selected account {account_number}")
                return

        print(f"Account {account_number} not found")

    def display_menu(self):
        print("1. Open account")
        print("2. Close account")
        print("3. Select account")
        print("4. Query account information")
        print("5. Exit")
 
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
                self.select_account(account_number)
            elif choice == "4":
                if self.current_account is None:
                    print("No account selected")
                else:
                    self.current_account.query_information()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

# Instantiate the BankApplication class and run the application
if __name__ == "__main__":
    bank_app = BankApplication()
    bank_app.run()
