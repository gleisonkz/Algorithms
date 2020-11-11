from RaceCar import RaceCar

firstCar = RaceCar(1, 'Test', 'Team 1', 120.00)
print(firstCar.currentSpeed)
firstCar.turnOn()
firstCar.speedUp(50)
print(firstCar.currentSpeed)
