"""
Prog 2
W02
P01 2.3 BankAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 08.03.2024
"""

import random

class BankAccount:
    # Class variable holding the list of all generated IBANs
    iban_list = []
    # Dictionary mapping currency codes to their symbols and subunits
    currency_dict = {
        "CHF": ["Fr.", "Rp."],
        "EUR": ["€", "Cent"],
        "USD": ["$", "¢"]
    }

    def __init__(self, owner, currency="CHF", balance=0.0):
        # Initialize a bank account; checks if the provided currency is supported
        if currency in BankAccount.currency_dict:
            self.account_number = BankAccount.generate_iban_numb(12)  # Generates a 12-digit account number
            self.iban = self.generate_iban()  # Generates a unique IBAN for the account
            self.owner = owner  # Account owner name
            self.__balance = balance  # Account balance, private attribute
            self.currency = currency  # Currency of the account
            print("Bank account Created")
        else:
            print(f"{currency} is not an accepted or valid currency. Therefore, your account will get terminated")
            BankAccount.close_account(self)

    @staticmethod
    def generate_iban_numb(iterations):
        # Generates a string of random digits of specified length
        numbs = ""
        for i in range(iterations):
            numbs += str(random.randint(0, 9))
        return numbs

    @staticmethod
    def is_float(string):
        # Checks if a string can be converted to float
        try:
            float(string)
            return True
        except ValueError:
            return False

    def generate_iban(self):
        # Generates a unique IBAN for the account
        country_code = "CH"
        check_sum = BankAccount.generate_iban_numb(2)  # Generates a 2-digit checksum
        bank_code = BankAccount.generate_iban_numb(5)  # Generates a 5-digit bank code
        account_numb = str(self.account_number)
        iban = country_code + check_sum + bank_code + account_numb
        if iban in BankAccount.iban_list:
            return self.generate_iban()  # Recursively generates a new IBAN if duplicate
        else:
            BankAccount.iban_list.append(iban)
        return iban

    def check_balance(self):
        # Converts balance to currency format and returns as string
        main_amount, sub_amount = divmod(self.__balance, 1)
        sub_amount = round(sub_amount, 2)
        ret_main = f"{main_amount} {BankAccount.currency_dict[self.currency][0]}"
        ret_sub = f"{sub_amount} {BankAccount.currency_dict[self.currency][1]}"
        return f"{ret_main} {ret_sub}"

    def withdraw(self, amount):
        # Withdraws amount from the account if it is a valid float and sufficient balance exists
        if BankAccount.is_float(amount) and float(amount) >= 0:
            if self.__balance < amount:
                print("Insufficient balance")
                return 0
            else:
                self.__balance -= amount
                print("Transaction successfully")
                return 1
        else:
            print("Invalid Input only positive Numbers are allowed")
            return 0

    def deposit(self, amount):
        # Deposits amount into the account if it is a valid float and does not exceed the limit
        if BankAccount.is_float(amount) and float(amount) >= 0 and self.__balance + amount <= 100000:
            self.__balance += amount
            print("Transaction successfully")
            return 1
        else:
            print(f"Invalid Input only positive Numbers are allowed or the balance exceeded 100k {self.currency}")
            return 0

    def close_account(self):
        # Delete the Iban because its no more needed
        BankAccount.iban_list.remove(self.iban)
        # Closes the bank account
        del self
        print("Bank account successfully closed")

# Main block to create an instance of BankAccount and test its methods
if __name__ == "__main__":
    # Below code is commented out and intended for testing purposes.
    """
    acc1 = BankAccount("Gian Gamper", "USD")
    print(acc1.iban)
    print(acc1.owner)
    print(acc1.currency)
    print(acc1.check_balance())

    acc1.withdraw(-20000)
    acc1.deposit(100000.2)
    acc1.withdraw(1.1)
    print(acc1.check_balance())
    """
