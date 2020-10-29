class Account:
    def __init__(self, accountID):
        self.AccountID = accountID
        self.balance = 0.0

    def showBalance(self):
        return self.balance

    def deposit(self, value):
        self.balance += value

    def withdrown(self, value):
        self.balance -= value

    def transfer(self, account, value):
        self.balance -= value
        account.balance += value
