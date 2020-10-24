def tryParseInt(message):
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


peoples = [{"name": input("type a name: "), "age": tryParseInt(
    "type an age: ")} for item in range(3)]


print(peoples)


def removeLessThanAge18(dictionary):
    return [{age for (age) in people.items() if people['age'] >= 18} for people in peoples]


filteredPeoples = removeLessThanAge18(peoples)

for item in enumerate(filteredPeoples):
    print(item)
