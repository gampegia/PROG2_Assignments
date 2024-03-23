class TaxReport:
    def __init__(self, accounts):
        self.accounts = accounts

    def total_balance_savings(self):
        balance_savings = 0
        for account in self.accounts:
            if account.type == "savings":
                balance_savings += account.get_amount()
        return balance_savings

    def total_balance_youth(self):
        balance_youth = 0
        for account in self.accounts:
            if account.type == "youth":
                balance_youth += account.get_amount()
        return balance_youth


if __name__ == "__main__":
    tax_report = TaxReport()
    tax_report.total_balance_youth(300)
    tax_report.total_balance_savings(500)
