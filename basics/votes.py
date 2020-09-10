from enum import Enum
from utils import Utils


class Votes(Enum):
    FirstCandidate = 1
    SecondCandidate = 2
    ThirdCandidate = 3
    FourthCandidate = 4
    Null = 5
    Blank = 6


TotalVotes = {
    Votes.FirstCandidate: 0,
    Votes.SecondCandidate: 0,
    Votes.ThirdCandidate: 0,
    Votes.FourthCandidate: 0,
    Votes.Null: 0,
    Votes.Blank: 0
}

Utils.showMessage("Starting")
votesToRegister = Utils.inputToInt("How many votes do you want to register?")

for usuario in range(votesToRegister):
    userVote = Utils.inputToInt("Vote:")
    candidateOption = Votes(userVote)
    TotalVotes[candidateOption] = TotalVotes[candidateOption] + 1

for vote, quantity in TotalVotes.items():
    print(f"{vote.name} - Qtd: {quantity}")
