class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self, value):
        self.balance += value

    def withdrown(self, value):
        self.balance -= value

    def transfer(self, account, value):
        self.balance -= value
        account.balance += value


class SavingAccount(Account):
    def __init__(self, number):
        super().__init__(number)
        self.__yield = 0

    def getYield(self):
        return self.__yield

    def applyYield(self, rate):
        self.__yield += super().getBalance() * rate / 100


obj = SavingAccount(1)
obj.deposit(200.0)
obj.applyYield(10)
print(obj.getBalance())
print(obj.getYield())
