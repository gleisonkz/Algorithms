function getDiscount(numberOfPeople) {
    const validations = [
        { validation: numberOfPeople < 10, value: 500 },
        { validation: numberOfPeople >= 10 && numberOfPeople < 25, value: 350 },
        { validation: numberOfPeople >= 25 && numberOfPeople < 100, value: 250 },
        { validation: numberOfPeople >= 100, value: 200 }
    ]
    return validations.find(c => c.validation).value
}
console.log(getDiscount(5))
console.log(getDiscount(11))
console.log(getDiscount(26))
console.log(getDiscount(500))


