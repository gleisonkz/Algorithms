from enum import Enum
from utils import Utils
from os import system


class Votes(Enum):
    FirstCandidate = 1
    SecondCandidate = 2
    ThirdCandidate = 3
    FourthCandidate = 4
    Null = 5
    Blank = 6


def showInvalidMessage() -> None:
    print("Invalid Option, Choose between 1 and 6")


def validateUserInput() -> int:
    optionVote = Utils.inputToInt("Vote:")
    if optionVote >= 1 and optionVote <= 6:
        return optionVote
    else:
        showInvalidMessage()
        return validateUserInput()


TotalVotes = {
    Votes.FirstCandidate: 0,
    Votes.SecondCandidate: 0,
    Votes.ThirdCandidate: 0,
    Votes.FourthCandidate: 0,
    Votes.Null: 0,
    Votes.Blank: 0
}

Utils.showMessage("Starting")
print("""
Choice an option Vote below :
[1] = Vote for First Candidate            
[2] = Vote for Second Candidate            
[3] = Vote for Third Candidate            
[4] = Vote for Fourth Candidate            
[5] = Vote Null
[6] = Vote Blank
""")
votesToRegister: int = Utils.inputToInt("How many votes do you want to register?")

for usuario in range(votesToRegister):
    userVote: int = validateUserInput()
    # userVote = validateUserInput(userVote)
    candidateOption = Votes(userVote)
    TotalVotes[candidateOption] = TotalVotes[candidateOption] + 1

system('cls||clear')
print("The Final Result is :")
for vote, quantity in TotalVotes.items():
    print(f"{vote.name} - Qtd: {quantity}")
