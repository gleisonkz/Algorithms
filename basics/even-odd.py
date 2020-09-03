import os

def tryParseInt(value):
    try:
        return int(value)
    except Exception:
        print("You must be input a integer value.")
        os._exit(0)

def isEvenOrOdd(number):
    types = ["Even", "Odd"]
    parsedNumber = tryParseInt(number)
    parsedNumber = parsedNumber % 2 != 0    
    return types[parsedNumber]

print(isEvenOrOdd(2))
print(isEvenOrOdd(1))
print(isEvenOrOdd("a"))
