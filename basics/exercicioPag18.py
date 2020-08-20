def getFruitName():
    return input("Write the fruit name: ")

fruit1 = {"name": getFruitName(), "value": 1.00}
fruit2 = {"name": getFruitName(), "value": fruit1["value"] * 2}
fruit3 = {"name": getFruitName(), "value": fruit1["value"] / 2}
fruit4 = {"name": getFruitName(), "value": fruit3["value"] * 3}
fruit5 = {"name": getFruitName(), "value": fruit4["value"] / 2}
fruits = [fruit1, fruit2, fruit3, fruit4, fruit5]
for fruit in fruits:
    print(f" Fruit {fruit['name']} costs {fruit['value']} R$")