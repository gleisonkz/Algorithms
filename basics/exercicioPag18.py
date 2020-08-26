def getFruitName():
    return input("Write the fruit name: ")

fruits = [
    {"name": getFruitName(), "value": 1.00},
    {"name": getFruitName(), "value": 1.00 * 2},
    {"name": getFruitName(), "value": 1.00 / 2},
    {"name": getFruitName(), "value": (1.00 / 2) * 3},
    {"name": getFruitName(), "value": ((1.00 / 2) * 3) / 2}]

for fruit in fruits:
    print(f" Fruit {fruit['name']} costs {fruit['value']} R$")