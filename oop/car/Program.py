from Car import Car

car1: Car = Car()
car2: Car = Car()
cars = [car1, car2]

for car in cars:
    car.model = input("Type the model: ")
    car.color = input("Type the color: ")
    car.year = input("Type the year: ")
    car.brand = input("Type the brand: ")
    car.chassis = input("Type the chassis: ")
    car.owner = input("Who's the owner? ")
    car.maxSpeed = input("What's the max speed? ")
    car.currentSpeed = input("What's the current speed? ")
    car.doorNumbers = input("How many doors? ")
    car.hasSunroof = input("Does it have sunroof? ")
    car.gearNumbers = input("How many gears? ")
    car.hasAutomaticGearBox = input("Does it have automatic gearbox?")
    car.fuelLevel = input("What's the current fuelLevel ?")

for index, car in enumerate(cars):
    print(f""" Car number {index + 1}
    Model: {car.model}    
    Color: {car.color}    
    Year: {car.year}    
    Brand: {car.brand}    
    Chassis: {car.chassis}    
    Owner: {car.owner}    
    MaxSpeed: {car.maxSpeed}    
    CurrentSpeed: {car.currentSpeed}    
    DoorNumbers: {car.doorNumbers}    
    HasSunroof: {car.hasSunroof}    
    GearNumbers: {car.gearNumbers}    
    HasAutomaticGearBox: {car.hasAutomaticGearBox}    
    FuelLevel: {car.fuelLevel}
    """)
