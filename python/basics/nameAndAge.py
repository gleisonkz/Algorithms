def tryParseInt(message):
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


peoples = {input("type a name: "): tryParseInt("type an age: ") for i in range(3)}


def removeLessThanAge18(dictionary):
    return {name: age for (name, age) in dictionary.items() if age >= 18}


filteredPeoples = removeLessThanAge18(peoples)
