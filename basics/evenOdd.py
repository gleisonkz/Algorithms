import os

def tryParseInt(value):
    try:
        return int(value)
    except:
        print("Coffin Dance")
        os._exit(0)

def isEvenOrOdd(number):
    parsedNumber = tryParseInt(number)
    parsedNumber = parsedNumber % 2 != 0
    types = ["Even", "Odd"]
    return types[parsedNumber]

print(isEvenOrOdd(2))
print(isEvenOrOdd(1))
print(isEvenOrOdd("a"))
