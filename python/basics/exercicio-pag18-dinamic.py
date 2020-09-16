def getUserInput(message="Write the fruit name: "):
    return input(message)


fruit1 = {"name": getUserInput(), "value": getUserInput("Write de price: ")}
fruit2 = {"name": getUserInput(), "value": float(fruit1['value']) * 2}
fruit3 = {"name": getUserInput(), "value": float(fruit1['value']) / 2}
fruit4 = {"name": getUserInput(), "value": (float(fruit1['value']) / 2) * 3}
fruit5 = {"name": getUserInput(), "value": (
    (float(fruit1['value']) / 2) * 3) / 2}

fruits = [fruit1, fruit2, fruit3, fruit4, fruit5]
for fruit in fruits:
    print(f" Fruit {fruit['name']} costs {fruit['value']} R$")
