from Account import Account
from time import sleep
import sys
import os


class ATM:
    currentAccount = None

    def __init__(self, currentAccount) -> None:
        os.system('cls||clear')
        self.currentAccount = currentAccount

    def showMenu(self):
        print("************Welcome to Account Bank**************")

        action = self.getUserOption()

        if action == 1:
            print(self.currentAccount.showBalance())
            self.loading('self.loading')
            self.showMenu()
        elif action == 2:
            value = self.tryParseInt("How much do you want to withdraw? ")
            self.currentAccount.withdrown(value)
            self.loading('withdrawing')
            self.showMenu()
        elif action == 3:
            value = self.tryParseInt("How much do you want to deposit? ")
            self.currentAccount.deposit(value)
            self.loading('depositing')
            self.showMenu()
        elif action == 4:
            newAccountID = input(
                "Type the accountID do you want to transfer to?")
            newAccount = Account(newAccountID)
            value = self.tryParseInt("How much do you want to transfer? ")
            self.currentAccount.transfer(newAccount, value)
            self.loading('transfering')
            self.showMenu()
        elif action == 5:
            self.loading('exiting')
            sys.exit()
        else:
            self.showMenu()

    def tryParseInt(self, message: str) -> int:
        try:
            return int(input(message))
        except ValueError:
            print("You must be input a integer value.")
            return self.tryParseInt(message)

    def getUserOption(self) -> int:
        return self.tryParseInt("""
        1: Show Balance
        2: Withdrown
        3: Deposit
        4: Transfer
        5: Exit

        Please enter your choice: """)

    def loading(self, message) -> None:
        for index in range(8):
            dots = [
                f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
                f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
            ]
            print(f"{dots[index]}", end="\r")
            sleep(0.2)
            pass
