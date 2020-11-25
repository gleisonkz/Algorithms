class UnityConversor:
    @staticmethod
    def meterToFeet(value):
        return value * 10.76

    @staticmethod
    def feetToCent(value):
        return value * 30.48

    @staticmethod
    def mileToAcre(value):
        return value * 640

    @staticmethod
    def acreToFeet(value):
        return value * 43560


print(UnityConversor.meterToFeet(5))
print(UnityConversor.feetToCent(5))
print(UnityConversor.mileToAcre(5))
print(UnityConversor.acreToFeet(5))
