from datetime import datetime
import os

def validateDate(day, month, year):
    try:
        return datetime(int(year), int(month), int(day))
    except ValueError:
        print("Invalid date")
        os._exit(0)

inputDate = input("Enter the date in format 'dd/mm/yy' : ")
day, month, year = inputDate.split('/')
validDate = validateDate(day, month, year).date().__format__("%d/%m/%y")
print(f"The date {validDate} is valid")
