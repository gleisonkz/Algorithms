class RaceCar:
    carID: int = None
    pilot: str = None
    team: str = None
    maxSpeed: float = None
    currentSpeed: float = None
    isTurnOn: bool = None

    def __init__(self, carID: int, pilot: str, team: str, maxSpeed: float):
        self.carID = carID
        self.pilot = pilot
        self.team = team
        self.maxSpeed = maxSpeed

    def setCurrentSpeed(self, speed: float):
        self.currentSpeed = speed if speed <= self.maxSpeed else print(
            "You can't exceed the maximum speed")

    def checkIfIsTurnOn(self, callback, args):
        callback(args) if self.isTurnOn == True else print("Car's off")

    def speedUp(self, unit: float):
        self.checkIfIsTurnOn(self.setCurrentSpeed, unit)

    def speedDown(self, percentage: float):
        self.checkIfIsTurnOn(self.setCurrentSpeed, percentage)

    def stop(self):
        self.currentSpeed = 0

    def turnOn(self):
        self.isTurnOn = True

    def turnOff(self):
        self.isTurnOn = False if self.currentSpeed == 0 else print(
            "Your car needs to be stopped to turn off.")
