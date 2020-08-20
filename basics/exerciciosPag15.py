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

getUserValue(items, quantity, 0)
getUserValue(items, quantity, 1)
getUserValue(items, quantity, 2)
getUserValue(items, quantity, 3)
getUserValue(items, quantity, 4)

def printValues(items, quantity, position):
    print(f"Item {position + 1} - {items[position]} | Qtd: {quantity[position]}")

printValues(items, quantity, 0)
printValues(items, quantity, 1)
printValues(items, quantity, 2)
printValues(items, quantity, 3)
printValues(items, quantity, 4)

# Exercicio 03 - Utilizando For
items = [None] * 5
quantity = [None] * 5
for i in range(5):
    items[i] = input("Informe um item: ")
    quantity[i] = input("Qual a quantidade?")

for i in range(5):
    print(f"Item {i + 1} - {items[i]} | Qtd: {quantity[i]}")
