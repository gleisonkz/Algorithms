from random import randint
from time import sleep
from enum import Enum
import os


class NumberState(Enum):
    Hot = "It's hot, it's hot"
    Cold = "It's hot, it's hot"


def exitGame(message: str) -> None:
    print(message)
    loading("LEAVING")
    os._exit(0)


def showNumberState(numberState: NumberState):
    print(numberState.value)


def youLoose(number: int) -> None:
    exitGame(f"You loose, I thought in {number}")


def youWin() -> None:
    exitGame("Congratulations, You Guess Right!")


def loading(message: str) -> None:
    for index in range(8):
        dots = [
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
        ]
        print(f"{dots[index]}", end="\r")
        sleep(0.2)
        pass


def tryParseInt(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


playerRemainingTries: int = 3
factor: int = 5
os.system('cls||clear')
cpuChoice: int = randint(1, 100)

cpuChoiceMinRange: int = cpuChoice - 5
cpuChoiceMaxRange: int = cpuChoice + 5
print("I'll think a number, TRY TO GUESS...")
sleep(2)


while playerRemainingTries > 0:
    playerChoice = tryParseInt("In what number did I think?")

    if playerChoice != cpuChoice and playerChoice >= cpuChoiceMinRange and playerChoice <= cpuChoiceMaxRange:
        showNumberState(NumberState.Hot)
    elif playerChoice == cpuChoice:
        youWin()
    elif playerRemainingTries > 1:
        showNumberState(NumberState.Cold)
    playerRemainingTries -= 1
youLoose(cpuChoice)
