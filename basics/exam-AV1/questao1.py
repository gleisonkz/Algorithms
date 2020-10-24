def tryParseInt(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


def factorial(number: int) -> int:
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


number: int = tryParseInt("Type a number : ")
print(f"The number {number} factorial is: {factorial(number)}")
