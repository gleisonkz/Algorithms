from enum import Enum


class Meses(Enum):
    Janeiro = 1
    Fevereiro = 2
    Marco = 3
    Abril = 4
    Maio = 5
    Junho = 6
    Julho = 7
    Agosto = 8
    Setembro = 9
    Outubro = 10
    Novembro = 11
    Dezembro = 12


monthsTemperature = {
    Meses.Janeiro: 0,
    Meses.Fevereiro: 0,
    Meses.Marco: 0,
    Meses.Abril: 0,
    Meses.Maio: 0,
    Meses.Junho: 0,
    Meses.Julho: 0,
    Meses.Agosto: 0,
    Meses.Setembro: 0,
    Meses.Outubro: 0,
    Meses.Novembro: 0,
    Meses.Dezembro: 0,
}

for month in Meses:
    currentValue = int(input(f"Insira a temperatura para o mês de {month.name}: "))
    monthsTemperature[month] = currentValue

temperaturesSum = sum(monthsTemperature.values())
temperaturesAverage = temperaturesSum / 12

print(f"A média anual das temperaturas é: {temperaturesAverage} ")
print("abaixo os meses que ficaram acima da média:")

for month, temperature in monthsTemperature.items():
    if temperature > temperaturesAverage:
        print(f"{month.name} : {temperature}")
