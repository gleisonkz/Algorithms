import os
from datetime import datetime


def exitGame(message):
    print(message)
    os._exit(0)


def validateMonth(month):
    (month <= 0 or month > 12) and exitGame("Invalid Month")


def validateDay(day, month, year):
    daysInMonth = [
        0, 31, getFebruaryDaysInYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    (day <= 0 or day > daysInMonth[month]) and exitGame("Invalid Day")


def validateYear(year):
    currentYear = datetime.now().year
    (year == 0 or year < currentYear)


def isLeapYear(year):
    def divisibleBy(number): return year % number == 0
    result = divisibleBy(4) and not(divisibleBy(100)) and divisibleBy(400)
    return result


def getFebruaryDaysInYear(year):
    days = [28, 29]
    return days[isLeapYear(year)]


fullDate = input("Enter the date in format 'dd/mm/yy' : ")
day, month, year = map(int, fullDate.split('/'))
validateMonth(month)
validateDay(day, month, year)
validateYear(year)
print("Your date is valid.")
