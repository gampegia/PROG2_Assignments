class TaxReport:
    """
    A class to generate tax reports for accounts.

    Attributes:
        accounts (list): A list of account instances.

    Methods:
        __init__(accounts): Initializes the TaxReport instance with a list of accounts.
        total_balance_savings(): Returns the total balance of all savings accounts.
        total_balance_youth(): Returns the total balance of all youth accounts.
    """

    def __init__(self, accounts):
        """
        Initializes the TaxReport instance with a list of accounts.

        Args:
            accounts (list): A list of account instances.
        """
        self.accounts = accounts

    def total_balance_savings(self):
        """
        Returns the total balance of all savings accounts.

        Returns:
            float: The total balance of all savings accounts.
        """
        balance_savings = 0
        for account in self.accounts:
            if account.type == "savings":
                balance_savings += account.get_amount()
        return balance_savings

    def total_balance_youth(self):
        """
        Returns the total balance of all youth accounts.

        Returns:
            float: The total balance of all youth accounts.
        """
        balance_youth = 0
        for account in self.accounts:
            if account.type == "youth":
                balance_youth += account.get_amount()
        return balance_youth


if __name__ == "__main__":
    tax_report = TaxReport()
    tax_report.total_balance_youth(300)
    tax_report.total_balance_savings(500)