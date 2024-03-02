"""


Class Structure :

constructors:
Inhaber
IBAN
currenzy
money balance



Methods:
generate iban
Withdraw
deposit
see balance
open
close

"""

import random





class bankaccount:
    iban_list = []

    def __int__(self, iban, owner, currency, balance=0.0):
        self.iban = iban
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.account_number = bankaccount.generate_iban_numb(12)
    @staticmethod
    def generate_iban_numb(iterations):
        numbs = ""
        for i in range(iterations):
            numbs += str(random.randint(0, 9))

        return numbs
    def generate_iban(self):
        country_code = "CH"
        check_sum = bankaccount.generate_iban_numb(2)
        bank_code = bankaccount.generate_iban_numb(5)
        account_numb = str(self.account_number)
        iban = country_code + check_sum + bank_code + account_numb
        if iban in bankaccount.iban_list:
            return self.generate_iban()
        else:
            bankaccount.iban_list.append(iban)
        return iban
