
from ExchangeRates import ExchangeRates
from SavingsAccount import SavingsAccount
from YouthAccount import YouthAccount

from BankAccount import BankAccount


class TaxReport:
    """
    A class to generate tax reports for accounts.

    Attributes:
        accounts (list): A list of account instances.

    Methods:
        __init__(accounts): Initializes the TaxReport instance with a list of accounts.
        total_balance_savings(): Returns the total balance of all savings accounts in CHF.
        total_balance_youth(): Returns the total balance of all youth accounts in CHF.

    """

    def __init__(self, accounts):
        """
        Initializes the TaxReport instance with a list of accounts.

        Args:
            accounts (list): A list of account instances.
        """
        self.accounts = accounts
        self.exchange_rates = ExchangeRates()

    def total_balance_savings(self):
        """
        Returns the total balance of all savings accounts in CHF.

        Returns:
            float: The total balance of all savings accounts in CHF.
        """
        balance_savings = 0
        for account in self.accounts:
            if account.type == "savings":
                if account.currency == "USD":
                    balance_savings += self.exchange_rates.get_usd_chf(account.get_amount())
                elif account.currency == "EUR":
                    balance_savings += self.exchange_rates.get_eur_chf(account.get_amount())
                else:
                    balance_savings += account.get_amount()
        return balance_savings


    def total_balance_youth(self):
        """
        Returns the total balance of all youth accounts in CHF.

        Returns:
            float: The total balance of all youth accounts in CHF.
        """
        balance_youth = 0
        for account in self.accounts:
            if account.type == "youth":
                if account.currency == "USD":
                    balance_youth += self.exchange_rates.get_usd_chf(account.get_amount())
                elif account.currency == "EUR":
                    balance_youth += self.exchange_rates.get_eur_chf(account.get_amount())
                else:
                    balance_youth += account.get_amount()
        return balance_youth
    

if __name__ == "__main__":
    # Erstellen Sie einige Kontoinstanzen
    account1 = SavingsAccount("Owner1", currency="CHF")
    account2 = YouthAccount("Owner2", "01-01-2000", currency="EUR")
    # Fügen Sie die Konten in eine Liste ein
    accounts = [account1, account2]

    # Erstellen Sie eine Instanz von TaxReport mit der Liste der Konten
    tax_report = TaxReport(accounts)
    print(tax_report.total_balance_youth())
    print(tax_report.total_balance_savings())
