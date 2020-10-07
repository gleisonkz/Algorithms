def tryParseInt(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


def printEvenNumber(number: int) -> None:
    if number % 2 == 0:
        print(number)


initialRange: int = tryParseInt("type the initial range: ")
finalRange: int = tryParseInt("type the final range: ")

for number in range(initialRange, finalRange + 1):
    printEvenNumber(number)
