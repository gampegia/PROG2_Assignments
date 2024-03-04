"""


Class Structure :

constructors:
Inhaber
IBAN
currenzy
money balance



Methods:
+generate iban
+Withdraw
+deposit
+see balance
+open
+close

"""

import random


class get_Bankaccount:
    iban_list = []
    currency_dict = {
        "CHF": ["Fr.", "Rp."],
        "EUR": ["€", "Cent"],
        "USD": ["$", "¢"]
    }

    def __init__(self, owner, currency="CHF", balance=0.0):
        if currency in get_Bankaccount.currency_dict:
            self.account_number = get_Bankaccount.generate_iban_numb(12)
            self.iban = self.generate_iban()
            self.owner = owner
            self.__balance = balance
            self.currency = currency
            print("Bankaccount Created")
        else:
            print(currency,"Is not a accepted or valid currency. Therefor your account will get terminated")
            get_Bankaccount.close_account(self)



    @staticmethod
    def generate_iban_numb(iterations):
        numbs = ""
        for i in range(iterations):
            numbs += str(random.randint(0, 9))

        return numbs
    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    def generate_iban(self):
        country_code = "CH"
        check_sum = get_Bankaccount.generate_iban_numb(2)
        bank_code = get_Bankaccount.generate_iban_numb(5)
        account_numb = str(self.account_number)
        iban = country_code + check_sum + bank_code + account_numb
        if iban in get_Bankaccount.iban_list:
            return self.generate_iban()
        else:
            get_Bankaccount.iban_list.append(iban)
        return iban

    def check_balance(self):
        # Umrechnung von Rappen in Franken und Rappen für die Anzeige
        main_amount,sub_amount = divmod(self.__balance,1)
        sub_amount = round(sub_amount,2)
        ret_main = f"{main_amount} {get_Bankaccount.currency_dict[self.currency][0]}"
        ret_sub = f"{sub_amount} {get_Bankaccount.currency_dict[self.currency][1]}"
        return f"{ret_main} {ret_sub}"


    def withdraw(self, amount):
        if get_Bankaccount.is_float(amount) and float(amount) >= 0:
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
        if get_Bankaccount.is_float(amount) and float(amount) >= 0 and self.__balance + amount <= 100000:
            self.__balance += amount
            print("Transaction successfully")
            return 1
        else:
            print(f"Invalid Input only positive Numbers are allowed or the balance exeeded 100k {self.currency}")
            return 0

    def close_account(self):
        del self
        print("Bank account successfully closed")


if __name__ == "__main__":
    acc1 = get_Bankaccount("Gian Gamper","UDR")
    while 1:
        print("1")

    """ 
    print(acc1.iban)
    print(acc1.owner)
    print(acc1.currency)
    print(acc1.check_balance())

    acc1.withdraw(-20000)
    acc1.deposit(100000.2)
    acc1.withdraw(1.1)
    print(acc1.check_balance())"""