"""
Prog 2
W02
P01 2.3 BankAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 08.03.2024
"""

import random  # Importing the random module for generating random numbers


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        iban_list (list): A class variable that stores all generated IBANs to ensure uniqueness.
        currency_dict (dict): A class variable that maps currency codes to their symbols and subunits.
    """

    # Class variable holding the list of all generated IBANs
    iban_list = []

    # Dictionary mapping currency codes to their symbols and subunits
    currency_dict = {
        "CHF": ["Fr.", "Rp."],
        "EUR": ["€", "Cent"],
        "USD": ["$", "¢"]
    }

    def __init__(self, owner, currency="CHF", balance=0.0):
        """
        Initializes a BankAccount instance.

        Args:
            owner (str): The name of the account owner.
            currency (str, optional): The currency of the account. Defaults to 'CHF'.
            balance (float, optional): The initial balance of the account. Defaults to 0.0.

        Prints a message indicating account creation or an error if the currency is not supported.
        """
        if currency in BankAccount.currency_dict:
            self.account_number = BankAccount.generate_iban_numb(12)  # Generates a 12-digit account number
            self.iban = self.generate_iban()  # Generates a unique IBAN for the account
            self.owner = owner  # Account owner name
            self.__balance = balance  # Account balance, private attribute
            self.currency = currency  # Currency of the account
            print("Bank account Created")
        else:
            print(f"{currency} is not an accepted or valid currency. Therefore, your account will get terminated")
            self.close_account()

    @staticmethod
    def generate_iban_numb(iterations):
        """
        Generates a string of random digits of specified length.

        Args:
            iterations (int): The number of digits to generate.

        Returns:
            str: A string of random digits.
        """
        numbs = ""
        for i in range(iterations):
            numbs += str(random.randint(0, 9))
        return numbs

    @staticmethod
    def is_float(string):
        """
        Checks if a string can be converted to float.

        Args:
            string (str): The string to check.

        Returns:
            bool: True if the string can be converted to float, False otherwise.
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def generate_iban(self):
        """
        Generates a unique IBAN for the account.

        Returns:
            str: A unique IBAN.
        """
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
        """
        Converts the account balance to currency format and returns it as a string.

        Returns:
            str: The account balance in currency format.
        """
        main_amount, sub_amount = divmod(self.__balance, 1)
        sub_amount = round(sub_amount, 2)
        ret_main = f"{main_amount} {BankAccount.currency_dict[self.currency][0]}"
        ret_sub = f"{sub_amount} {BankAccount.currency_dict[self.currency][1]}"
        return f"{ret_main} {ret_sub}"

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if it is a valid float and if sufficient balance exists.

        Args:
            amount (str): The amount to withdraw.

        Returns:
            int: 1 if the transaction is successful, 0 otherwise.
        """
        if BankAccount.is_float(amount) and float(amount) >= 0:
            if self.__balance < float(amount):
                print("Insufficient balance")
                return 0
            else:
                self.__balance -= float(amount)
                print("Transaction successfully")
                return 1
        else:
            print("Invalid Input only positive Numbers are allowed")
            return 0

    def deposit(self, amount):
        """
        Deposits a specified amount into the account if it is a valid float and does not exceed the limit.

        Args:
            amount (str): The amount to deposit.

        Returns:
            int: 1 if the transaction is successful, 0 otherwise.
        """
        if BankAccount.is_float(amount) and float(amount) >= 0 and self.__balance + float(amount) <= 100000:
            self.__balance += float(amount)
            print("Transaction successfully")
            return 1
        else:
            print(f"Invalid Input only positive Numbers are allowed or the balance exceeded 100k {self.currency}")
            return 0

    def close_account(self):
        """
        Closes the bank account and removes its IBAN from the list of generated IBANs.
        """
        BankAccount.iban_list.remove(self.iban)
        print("Bank account successfully closed")
        del self


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
