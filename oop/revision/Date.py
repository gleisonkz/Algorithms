import os


class Date:
    day = None
    month = None
    year = None

    def init(self, day, month, year):
        self.month = self.validateMonth(month)
        self.day = self.validateDay(day)
        self.year = self.validateYear(year)

    def validateMonth(self, month):
        (month <= 0 or month > 12) and self.sair('month invalido')
        return month

    def validateDay(self, day):
        daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        (day <= 0 or day > daysInMonth[self.month]) and self.sair('day invalido')
        return day

    def validateYear(self, year):
        year <= 0 and self.sair('year invalido')

    def sair(self, mensagem):
        print(mensagem)
        os._exit(0)
