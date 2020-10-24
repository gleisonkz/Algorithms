def printMultiplicationTable(number: int) -> None:
    for index in range(0, 11):
        print(f"{index} x {number} = {number*index}")


printMultiplicationTable(int(input("enter a number:")))
