from questao3 import Pen

pens = []

for index in range(3):
    pen = Pen(
        input("Type the color: "),
        input("This pen has ink?"),
        input("Is this pen opened?"),
        input("Type the brand: ")
    )
    pens.append(pen)


for index, pen in enumerate(pens):
    print(f"""
    Color: {pen.color}    
    Has Ink: {pen.hasInk}    
    Is Opened: {pen.isOpened}    
    Brand: {pen.brand}   
    """)
