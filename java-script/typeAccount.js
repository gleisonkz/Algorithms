const getAccType = (accType) => {
    const types = {
        PLATINUM: 'Platinum Customer',
        GOLD: 'Gold Customer',
        SILVER: 'Silver Customer',
    }
    return types[accType]
}
console.log(getAccType("PLATINUM"))
console.log(getAccType("GOLD"))
console.log(getAccType("SILVER"))