class Calculator:
    lastResult = 0

    def sum(self, number1, number2):
        result = number1 + number2
        self.lastResult = result
        return result

    def getLastResult(self):
        return self.lastResult

    @staticmethod
    def subtraction(number1, number2):
        return number1 - number2
