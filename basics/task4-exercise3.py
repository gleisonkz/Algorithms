totalPerson = 5

beer = (75 * 2.20)
spaghetti = (2 * 8.73)
tomatoSauce = 3.45
onion = (5.40 * 420 / 1000)
garlic = (30 * 250 / 1000)
frenchBread = (25 * 450 / 1000)
totalPrice = (
    beer + spaghetti +
    tomatoSauce + onion +
    garlic + frenchBread) / totalPerson
print(f"The price for each people is {totalPrice:.2f}")
