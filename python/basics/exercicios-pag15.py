# Exercicio 01
print("Hello World")

# Exercicio 02
number = input("Type a number: ")
print(f"The number typed was {number}")

# Exercicio 03 - sem estrutura de repetição
items = [None] * 5
quantity = [None] * 5


def getUserValue(items, quantity, position):
    items[position] = input("Informe um item: ")
    quantity[position] = input("Qual a quantidade?")


def printValues(items, quantity, position):
    print(
        f"Item {position + 1} - {items[position]} | Qtd: {quantity[position]}")


getUserValue(items, quantity, 0)
getUserValue(items, quantity, 1)
getUserValue(items, quantity, 2)
getUserValue(items, quantity, 3)
getUserValue(items, quantity, 4)

printValues(items, quantity, 0)
printValues(items, quantity, 1)
printValues(items, quantity, 2)
printValues(items, quantity, 3)
printValues(items, quantity, 4)

# Exercicio 03 - Utilizando For


def tryParseInt(message):
    try:
        return int(input(message))
    except ValueError:
        print("You must be input a integer value.")
        return tryParseInt(message)


items = [{
    "key": input("Informe um item: "),
    "value": tryParseInt("Qual a quantidade? ")}
    for item in range(5)]
for index, item in enumerate(items):
    print(f"Item {index + 1} | Value: {item['key']} | Qtd: {item['value']}")
