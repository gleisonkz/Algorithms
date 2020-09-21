const getAccountType = (accountType) => {
    const types = {
        PLATINUM: 'Platinum Customer',
        GOLD: 'Gold Customer',
        SILVER: 'Silver Customer',
    }
    return types[accountType]
}
console.log(getAccountType("PLATINUM"))
console.log(getAccountType("GOLD"))
console.log(getAccountType("SILVER"))
