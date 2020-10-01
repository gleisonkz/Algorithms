import os


def tryParseInt(value):
    try:
        return int(value)
    except Exception:
        print("You must be input a integer value.")
        os._exit(0)


number = None
flag = qtdNumbers = qtdNumbersEven = qtdNumbersOdd = evenSum = totalSum = 0

while number != flag:
    number = tryParseInt(input("Insira um numero positivo: "))
    if number % 2 == 0:
        qtdNumbersEven += 1
        evenSum += number
    else:
        qtdNumbersOdd += 1

    totalSum += number
    qtdNumbers += 1

print(f"O total de números pares é: {qtdNumbersEven}")
print(f"O total de números impares é:  {qtdNumbersOdd}")
print(f"A média dos números pares é :  {evenSum / qtdNumbersEven}")
print(f"O média geral dos números é:  {totalSum / qtdNumbers}")
