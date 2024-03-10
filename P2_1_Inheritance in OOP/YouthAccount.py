"""
Prog 2
W02
P01 3.1 YouthAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 10.03.2024
"""

from BankAccount import BankAccount
from datetime import datetime
import re

class SavingsAccount(BankAccount):
    # Constants
    NEGATIVE_BALANCE_ALLOWED = False
    DATE_FORMAT = "%d-%m-%Y"
    MONTHLY_WITHDRAWAL_LIMIT = 2000
    WITHDREW_THIS_MONTH = 0

    def __init__(self, owner, date_of_birth, balance=0.0, monthly_interest_rate=0.001):
        super().__init__(owner, balance=balance)
        self.date_of_birth = date_of_birth
        self.monthly_interest_rate = monthly_interest_rate
        self.balance = balance
        if not self.is_younger_than_25():
            raise ValueError("Youth Account could not be created due to your age")

    def withdraw(self, amount):
        result = 0
        if BankAccount.is_float(amount) and float(amount) >= 0:
            if self.WITHDREW_THIS_MONTH < self.MONTHLY_WITHDRAWAL_LIMIT:
                if not SavingsAccount.NEGATIVE_BALANCE_ALLOWED:
                    if self.balance >= float(amount):
                        self.balance -= float(amount)
                        result = 1
                    else:
                        self.balance = 0



        else:
            result = 0
        return result

    def is_younger_than_25(self):
        try:
            # Convert input string to datetime object
            birthdate = datetime.strptime(self.date_of_birth, self.DATE_FORMAT)

            # Get the current date
            current_date = datetime.now()

            # Calculate the age
            age = (current_date.year - birthdate.year -
                   ((current_date.month, current_date.day) < (birthdate.month, birthdate.day)))

            # Check if the age is less than or equal to 25
            if age <= 25:
                result = True
            else:
                print("Too old to create a Youth Account")
                result = False
        except ValueError:
            print(f"Your birthdate dont matches the format '%d-%m-%Y'")
            result = False
        return result


# Main block to create an instance of BankAccount and test its methods
if __name__ == "__main__":
# Below code is commented out and intended for testing purposes.

    sa = SavingsAccount("Jonas", "22-01-1990")
    sa.deposit(5000)
    print(sa.check_balance())
    sa.withdraw(6000)
    print(sa.check_balance())


