from random import randint
from time import sleep
from enum import Enum
import os


class PlayerState(Enum):
    WINNER = "Congratulations, You Guess Right!"
    MISS = "You're wrong try again!"
    LOOSER = "You loose, I thought in another number"


def exitGame():
    loading("LEAVING")
    os._exit(0)


def doNothing():
    pass


def loading(message):
    for index in range(8):
        dots = [
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
        ]
        print(f"{dots[index]}", end="\r")
        sleep(0.2)
        pass


def tryParseInt(message):
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


def isGuessRight(playerOption, cpuOption, remainingChances):
    outputs = {
        playerOption == cpuOption[0]: PlayerState.WINNER,
        playerOption != cpuOption[0] and remainingChances > 1: PlayerState.MISS,
        playerOption != cpuOption[0] and remainingChances == 1: PlayerState.LOOSER
    }
    return outputs[True]


def isHotOrCold(playerOption: int, cpuOption: int) -> None:

    # outputs = {
    #     playerOption == cpuOption[0]: PlayerState.WINNER,
    #     playerOption != cpuOption[0] and remainingChances > 1: PlayerState.MISS,
    # }

    # def isGameFinished(status, playerChoice, cpuChoice):
    #     outputs = {
    #         PlayerState.WINNER: exitGame,
    #         PlayerState.LOOSER: doNothing,
    #         PlayerState.MISS: isHotOrCold
    #     }
    #     outputs[status]()


playerRemainingTries = 3
os.system('cls||clear')
cpuChoice = [randint(1, 5)]
print("I'll think a number, TRY TO GUESS...")
sleep(2)

# while playerRemainingTries > 0:
#     playerChoice = input("In what number did I think?")
#     playerChoice = tryParseInt(playerChoice)
#     loading("LOADING")
#     isRight = isGuessRight(playerChoice, cpuChoice, playerRemainingTries)
#     infoMessage = isRight.value
#     print(infoMessage)
#     isGameFinished(isRight, playerChoice, cpuChoice)
#     playerRemainingTries -= 1
# exitGame()
