items = [{
    "key": input("Item name: "),
    "value": int(input("Quantity: "))}
    for item in range(5)]
for index, item in enumerate(items):
    print(f"Item {index + 1} | Value: {item['key']} | Qtd: {item['value']}")
