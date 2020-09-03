from random import randint
from time import sleep
from enum import Enum
import os

class PlayerState(Enum):
    WINNER = "Congratulations, You Guess Right!"
    MISS = "You're wrong try again!"
    LOOSER = "You loose, I thought in another number"
class LevelState(Enum):
    EASY = 1
    HARD = 2

def exitGame():
    loading("LEAVING")
    os._exit(0)

def loading(message):
    for index in range(8):
        dots = [
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
            f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
        ]
        print(f"{dots[index]}", end="\r")
        sleep(0.2)

def isGuessRight(playerOption, cpuOption, remainingChances):
    outputs = {
        playerOption == cpuOption[0]: PlayerState.WINNER,
        playerOption != cpuOption[0] and remainingChances > 1: PlayerState.MISS,
        playerOption != cpuOption[0] and remainingChances == 1: PlayerState.LOOSER
    }
    return outputs[True]

def validateInput(value):
    try:
        return int(value)
    except Exception:
        print("You must be input a integer value.")
        exitGame()

def doNothing():
    pass

def isGameFinished(status):
    outputs = {
        PlayerState.WINNER: exitGame,
        PlayerState.LOOSER: doNothing,
        PlayerState.MISS: doNothing
    }
    outputs[status]()

def refreshCpuChoice(level, choice):
    refresh = {
        LevelState.EASY: choice[0],
        LevelState.HARD: randint(1, 5)
    }
    choice[0] = refresh[level]

def convertInputToInt(message):
    value = input(message)
    return validateInput(value)

playerRemainingTries = 3
os.system('cls||clear')
cpuChoice = [randint(1, 5)]

userInputLevel = convertInputToInt("Choose the level game: [1] = EASY [2] = HARD: ")
currentLevel = LevelState(userInputLevel)
print("I'll think a number between 1 and 5!, TRY TO GUESS...")
sleep(2)

while playerRemainingTries > 0:
    refreshCpuChoice(currentLevel, cpuChoice)
    playerChoice = input("In what number did I think?")
    playerChoice = validateInput(playerChoice)
    loading("LOADING")
    isRight = isGuessRight(playerChoice, cpuChoice, playerRemainingTries)
    infoMessage = isRight.value
    print(infoMessage)
    isGameFinished(isRight)
    playerRemainingTries -= 1

exitGame()
