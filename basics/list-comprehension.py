def tryParseInt(message):
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


items = [{"key": input("Item name: "), "value": tryParseInt(
    "Quantity: ")} for item in range(5)]

for index, item in enumerate(items):
    print(f"Item {index + 1} | Value: {item['key']} | Qtd: {item['value']}")
