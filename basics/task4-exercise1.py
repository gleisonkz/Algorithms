# Exercise 01
import os

def tryParseInt(value):
    try:
        return int(value)
    except Exception:
        print("Coffin Dance")
        os._exit(0)

def getUserValue(message):
    value = input(message)
    value = tryParseInt(value)
    return value

def isAbleToVote(age):
    outputs = {
        age >= 18: "You are able to vote",
        age < 18: "You are not able to bote"
    }
    return outputs[True]

currentYear = 2020
personYear = getUserValue("Write your year of birth: ")
age = currentYear - personYear
message = isAbleToVote(age)
print(f"You're {age} years old, and {message}")
