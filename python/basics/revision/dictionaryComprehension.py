from enum import Enum


class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    Jun = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


monthsTemperature = {month: int(input(f"Type the current temperature for {month.name}: "))
                     for month in Months}

temperaturesSum = sum(monthsTemperature.values())
temperaturesAverage = temperaturesSum / 12
print(f" Temperature's total average is : {temperaturesAverage} ")
print("below the months above average:")

for month, temperature in monthsTemperature.items():
    if temperature > temperaturesAverage:
        print(f"{month.name} : {temperature}")
