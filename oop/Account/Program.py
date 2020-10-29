from Account import Account

account1 = Account(1)
account2 = Account(2)


account1.deposit(10)
account2.deposit(5)

print(account1.showBalance())
print(account2.showBalance())

account1.transfer(account2, 5)

print(account1.showBalance())
print(account2.showBalance())
