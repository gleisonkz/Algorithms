from typing import Dict


def getStudentStatus(note: int) -> str:
    validations: Dict[bool, str] = {
        note > 6: "Aprovado",
        note >= 4 and note <= 6: "Verificação Suplementar",
        note < 4: "Reprovado"
    }
    return validations[True]


def average(note1, note2):
    return (note1 + note2) / 2


firstAverage: float = average(5, 5)
print(getStudentStatus(firstAverage))

secondAverage: float = average(8, 6)
print(getStudentStatus(secondAverage))

thirdAverage: float = average(4, 3)
print(getStudentStatus(thirdAverage))
