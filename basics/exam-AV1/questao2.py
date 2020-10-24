def tryParseInt(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


def removeLessThanAge18(dictionary: dict):
    return {name: age for (name, age) in dictionary.items() if age >= 18}


numberOfPeople: int = tryParseInt("How many people do you want to register?")
peoples: dict = {input("type your name: "): tryParseInt("type your age: ")
                 for i in range(numberOfPeople)}

filteredPeoples: dict = removeLessThanAge18(peoples)
print(filteredPeoples)
