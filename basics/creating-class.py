class Computer:
    def __init__(self, brand, memory, graphicCard):
        self.Brand = brand
        self.Memory = memory
        self.GraphicCard = graphicCard
        self.StateOn = "Turning on...."
        self.StateOff = "Turning off...."

    def TurnOn(self):
        print(self.TurnOn)

    def TurnOff(self):
        print(self.TurnOff)

    def ShowThisComputerInformation(self):
        print(
            f"Brand: {self.Brand} | Memory: {self.Memory} | Graphic Card: {self.GraphicCard}")


pc1 = Computer("Asus", "6GB", "RX570")
pc2 = Computer("RG", "8GB", "Teste")
pc3 = Computer("LG", "4GB", "Teste")
pc1.ShowThisComputerInformation()
pc2.ShowThisComputerInformation()
pc3.ShowThisComputerInformation()
