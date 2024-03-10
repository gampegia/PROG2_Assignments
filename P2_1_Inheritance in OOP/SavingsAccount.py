"""
Prog 2
W02
P01 3.1 SavingsAccount

Authors:
Gwendoline Vocat (Vocatgwe), Gian Gamper (Gampegia), Jonas Bratschi (Bratsjon)

Date: 10.03.2024
"""

from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    # Constants
    PENALTY_INTEREST = 0.02
    NEGATIVE_BALANCE_ALLOWED = True

    def __init__(self, owner, balance=0.0, monthly_interest_rate=0.001):
        super().__init__(owner, balance=balance)
        self.monthly_interest_rate = monthly_interest_rate
        self.balance = balance

    def withdraw(self, amount):
        result = 0
        if BankAccount.is_float(amount) and float(amount) >= 0:
            if SavingsAccount.NEGATIVE_BALANCE_ALLOWED:
                if self.balance >= float(amount):
                    self.balance -= float(amount)
                    result = 1
                else:
                    if self.balance < 0:
                        penalty_amount = float(amount) * self.PENALTY_INTEREST
                        self.balance -= penalty_amount
                        result = 1
                    else:
                        penalty_amount = (float(amount) - self.balance) * self.PENALTY_INTEREST
                        self.balance -= (float(amount) + penalty_amount)
                        result = 1
        else:
            result = 0
        return result


# Main block to create an instance of BankAccount and test its methods
if __name__ == "__main__":
    # Below code is commented out and intended for testing purposes.
"""    
    sa = SavingsAccount("Jonas")
    sa.deposit(5000)
    print(sa.check_balance())
    sa.withdraw(7800)
    print(sa.check_balance())
"""
