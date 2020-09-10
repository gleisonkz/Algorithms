class Computer:
    Quantity = 0

    def __init__(self, brand, memory, graphicCard):
        self.Brand = brand
        self.Memory = memory
        self.GraphicCard = graphicCard
        self.StateOn = "Turning on...."
        self.StateOff = "Turning off...."
        Computer.Quantity += 1

    def TurnOn(self):
        print(self.TurnOn)

    def TurnOff(self):
        print(self.TurnOff)

    def ShowThisComputerInformation(self):
        return f"Brand: {self.Brand} | Memory: {self.Memory} | Graphic Card: {self.GraphicCard}"


computers = [
    Computer("Asus", "6GB", "RX570"),
    Computer("RG", "8GB", "Teste"),
    Computer("LG", "4GB", "Teste")
]

for index, computer in enumerate(computers):
    print(f"Computer {index + 1} - {computer.ShowThisComputerInformation()}")
print(Computer.Quantity)
