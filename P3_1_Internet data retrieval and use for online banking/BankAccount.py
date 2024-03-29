"""
Prog 2
W02
P01 2.3 BankAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 08.03.2024
"""

import random  # Importing the random module for generating random numbers
from ExchangeRates import ExchangeRates
import datetime

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
    DEFAULT_LAST_INTEREST = datetime.datetime.now()
    DEFAULT_INTEREST_RATE = 0
    def __init__(self, owner, currency="CHF", balance=0.0, negative_balance_allowed=False,
                 last_interest_dist=DEFAULT_LAST_INTEREST,monthly_interest_rate=DEFAULT_INTEREST_RATE):
        
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
            self.balance = balance  # Account balance, private attribute
            self.currency = currency  # Currency of the account
            self.__negative_balance_allowed = negative_balance_allowed
            self.last_interest_dist = last_interest_dist
            self.monthly_interest_rate = monthly_interest_rate
            BankAccount.status_notice("Bank account Created")
        else:
            BankAccount.status_notice(f"{currency} is not an accepted or valid currency. Therefore, "
                                      f"your account will get terminated")
            self.close_account()

    def apply_interest(self):
        if self.balance >= 0:
            timedelta = datetime.datetime.now() - self.last_interest_dist
            creditable_month = timedelta.total_seconds() / 10

            # for debug purpose print(creditable_month)
            self.balance *= (1 + (self.monthly_interest_rate * creditable_month))

    def reset_monthly_limit(self):
        self.withdrew_this_month = 0

    def check_interest_cycle(self):
        if datetime.datetime.now() - self.last_interest_dist >= datetime.timedelta(seconds=10):
            return_value = True
        else:
            return_value = False
        return return_value

    def process_month_end(self):
        self.apply_interest()
        self.reset_monthly_limit()
        self.reset_interest_dist_cycle()

    def reset_interest_dist_cycle(self):
        self.last_interest_dist = datetime.datetime.now()

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
        if self.check_interest_cycle():
            self.process_month_end()
        main_amount, sub_amount = divmod(self.balance, 1)
        sub_amount = round(sub_amount, 2)
        ret_main = f"{main_amount} {BankAccount.currency_dict[self.currency][0]}"
        ret_sub = f"{sub_amount} {BankAccount.currency_dict[self.currency][1]}"
        return f"{ret_main} {ret_sub}"

    def get_amount(self):
        if self.check_interest_cycle():
            self.process_month_end()
        return self.balance

    def withdraw(self, amount, currency="CHF"):
        """
        Withdraws a specified amount from the account if it is a valid float and if sufficient balance exists.

        Args:
            amount (str): The amount to withdraw.

        Returns:
            int: 1 if the transaction is successful, 0 otherwise.
        """
        if self.check_interest_cycle():
            self.process_month_end()


        if BankAccount.is_float(amount) and float(amount) >= 0:
            if currency and currency != self.currency:
                exchange_rates = ExchangeRates()
                if currency == "USD" and self.currency == "CHF":
                    amount = exchange_rates.get_usd_chf(float(amount))
                elif currency == "CHF" and self.currency == "USD":
                    amount = exchange_rates.get_chf_usd(float(amount))
                elif currency == "EUR" and self.currency == "USD":
                    amount = exchange_rates.get_eur_usd(float(amount))
                elif currency == "USD" and self.currency == "EUR":
                    amount = exchange_rates.get_usd_eur(float(amount))
                elif currency == "EUR" and self.currency == "CHF":
                    amount = exchange_rates.get_eur_chf(float(amount))
                elif currency == "CHF" and self.currency == "EUR":
                    amount = exchange_rates.get_chf_eur(float(amount))

            if not self.__negative_balance_allowed:
                if self.balance < float(amount):
                    BankAccount.status_notice("Insufficient balance")
                    result =  0
                else:
                    self.balance -= float(amount)
                    BankAccount.status_notice("Transaction successfully")
                    result = 1
            else:
                self.balance -= float(amount)
                BankAccount.status_notice("Transaction successfully")
                result = 1
        

        else:
            BankAccount.status_notice("Invalid Input only positive Numbers are allowed")
            result = 0
        return result

    def deposit(self, amount, currency="CHF"):
        """
        Deposits a specified amount into the account if it is a valid float and does not exceed the limit.

        Args:
            amount (str): The amount to deposit.

        Returns:
            int: 1 if the transaction is successful, 0 otherwise.
        """
        if self.check_interest_cycle():
            self.process_month_end()

        if BankAccount.is_float(amount) and float(amount) >= 0 and self.balance + float(amount) <= 100000:
            if currency and currency != self.currency:
                exchange_rates = ExchangeRates()
                if currency == "USD" and self.currency == "CHF":
                    amount = exchange_rates.get_usd_chf(float(amount))
                elif currency == "CHF" and self.currency == "USD":
                    amount = exchange_rates.get_chf_usd(float(amount))
                elif currency == "EUR" and self.currency == "USD":
                    amount = exchange_rates.get_eur_usd(float(amount))
                elif currency == "USD" and self.currency == "EUR":
                    amount = exchange_rates.get_usd_eur(float(amount))
                elif currency == "EUR" and self.currency == "CHF":
                    amount = exchange_rates.get_eur_chf(float(amount))
                elif currency == "CHF" and self.currency == "EUR":
                    amount = exchange_rates.get_chf_eur(float(amount))

            self.balance += float(amount)
            BankAccount.status_notice("Transaction successfully")
            result = 1
        else:
            BankAccount.status_notice(f"Invalid Input only positive Numbers are allowed or the balance exceeded 100k {self.currency}")
            result = 0
        return result

    @staticmethod
    def status_notice(string):
        print(string)
    def close_account(self):
        """
        Closes the bank account and removes its IBAN from the list of generated IBANs.
        """
        BankAccount.iban_list.remove(self.iban)
        BankAccount.status_notice("Bank account successfully closed")
        del self


# Main block to create an instance of BankAccount and test its methods
if __name__ == "__main__":
    # Below code is commented out and intended for testing purposes.

    acc1 = BankAccount("Gian Gamper", "USD", negative_balance_allowed=True)
    print(acc1.iban)
    print(acc1.owner)
    print(acc1.currency)
    print(acc1.check_balance())
    acc1.deposit(100)
    print(acc1.check_balance())
    acc1.withdraw(200)
    print(acc1.check_balance())
    
    acc1.withdraw(-20000)
    acc1.deposit(100000.2)
    acc1.withdraw(1.1)
    print(acc1.check_balance())

