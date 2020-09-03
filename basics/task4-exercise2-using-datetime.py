# Exercise 02
import datetime
import os

def validateDate(day, month, year):
    try:
        return datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print("Invalid date")
        os._exit(0)

inputDate = input("Enter the date in format 'dd/mm/yy' : ")
day, month, year = inputDate.split('/')
validDate = validateDate(day, month, year)
print(f"The date {validDate} is valid")
