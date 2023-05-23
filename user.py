class User:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.bank_accounts = []

    def link_bank_account(self, bank_account):
        self.bank_accounts.append(bank_account)


class BankAccount:
    def __init__(self, account_number, ifsc_code):
        self.account_number = account_number
        self.ifsc_code = ifsc_code
