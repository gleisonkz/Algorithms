import os
from datetime import datetime

def exit(message):
    print(message)
    os._exit(0)

def validateMonth(month):
    (month <= 0 or month > 12) and exit("Invalid Month")

def validateDay(day, month):
    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    (day <= 0 or day > daysInMonth[month]) and exit("Invalid Day")

def validateYear(year):
    currentYear = datetime.now().year
    (year == 0 or year < currentYear)

fullDate = input("Enter the date in format 'dd/mm/yy' : ")
day, month, year = map(int, fullDate.split('/'))
validateMonth(month)
validateDay(day, month)
validateYear(year)
print("Your date is valid.")
