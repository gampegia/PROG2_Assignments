"""
Prog 2
W02
P01 3.1 YouthAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 10.03.2024
"""
import time
from BankAccount import BankAccount
from datetime import datetime
import re

class YouthAccount(BankAccount):
    # Constants
    NEGATIVE_BALANCE_ALLOWED = False
    DATE_FORMAT = "%d-%m-%Y"
    MONTHLY_WITHDRAWAL_LIMIT = 2000
    WITHDREW_THIS_MONTH = 0
    DEFAULT_INTEREST_RATE_MONTH = 0.02

    def __init__(self, owner, date_of_birth, balance=0.0, monthly_interest_rate=DEFAULT_INTEREST_RATE_MONTH):
        super().__init__(owner, balance=balance)
        self.date_of_birth = date_of_birth
        self.monthly_interest_rate = monthly_interest_rate
        self.balance = balance
        self.withdrew_this_month = self.WITHDREW_THIS_MONTH
        if not self.is_younger_than_25():
            raise ValueError("Youth Account could not be created due to your age")

    def withdraw(self, amount):
        if self.check_interest_cycle():
            self.process_month_end()
        if BankAccount.is_float(amount) and float(amount) >= 0:
            if self.WITHDREW_THIS_MONTH < self.MONTHLY_WITHDRAWAL_LIMIT:
                if not YouthAccount.NEGATIVE_BALANCE_ALLOWED:
                    if self.MONTHLY_WITHDRAWAL_LIMIT - self.withdrew_this_month < float(amount):
                        if self.balance >= self.MONTHLY_WITHDRAWAL_LIMIT - self.withdrew_this_month:
                            self.balance -= self.MONTHLY_WITHDRAWAL_LIMIT - self.withdrew_this_month
                            self.withdrew_this_month = 2000
                            BankAccount.status_notice("Transaction successfully")
                        else:
                            self.balance = 0
                            self.withdrew_this_month += float(amount)
                            BankAccount.status_notice("Transaction successfully")
                    else:
                        if self.balance >= float(amount):
                            self.balance -= float(amount)
                            self.withdrew_this_month += float(amount)
                            BankAccount.status_notice("Transaction successfully")
                        else:
                            self.balance = 0
                            self.withdrew_this_month += float(amount)

        else:
            BankAccount.status_notice("Transaction Failed")
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
                BankAccount.status_notice("Too old to create a Youth Account")
                result = False
        except ValueError:
            BankAccount.status_notice(f"Your birthdate dont matches the format '%d-%m-%Y'")
            result = False
        return result


# Main block to create an instance of BankAccount and test its methods
if __name__ == "__main__":

# Below code is commented out and intended for testing purposes.

    sa = YouthAccount("Jonas", "22-01-1999")
    #YouthAccount.DEFAULT_INTEREST_RATE_MONTH = 1
    sa.monthly_interest_rate = 0.2
    print(YouthAccount.DEFAULT_INTEREST_RATE_MONTH)
    sa.deposit(1000)
    print(sa.check_balance())
    sa.withdraw(1000)
    print(sa.check_balance())
    sa.deposit(1100)
    print(sa.check_balance())
    sa.withdraw(1050)
    print(sa.check_balance())
    print(sa.withdrew_this_month)
    time.sleep(10)
    print(sa.check_balance())
    sa.withdraw(6000)
    print(sa.check_balance())



