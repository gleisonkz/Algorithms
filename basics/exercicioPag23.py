person = {
    "Name":"Gleison",
    "LastName":"Almeida",
    'Age':'26',
    "Course":"Sistemas de Informação",
    "Address":"Rua D, padrão 105 casa 07 - Betania"
}

print(person)

print(f"person['Name']")
print(person['LastName'])
print(person['Age'])
print(person['Course'])
print(person['Address'])

del person['Course']

person['LastName'] = "Lopes"

print(person)
print(person['Address'])

newPerson = person.copy()
newPerson['Name'] = 'Renato'
newPerson['Age'] = 20

print(newPerson)
print(person.values)






