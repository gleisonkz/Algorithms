import sys

def tryParseInt(value):
    try:
        num = int(value)
    except ValueError:
        print("Coffin Dance")
        sys.exit(True)
    return num % 2 == 0

def isEvenOrOdd(number):
    number = tryParseInt(number)
    types = ["Odd", "Even"]
    return types[number]

print(isEvenOrOdd(2))
print(isEvenOrOdd(1))
print(isEvenOrOdd("a"))
