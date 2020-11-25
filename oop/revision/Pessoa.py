class Person:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name

    def setAddress(self, address):
        self.address = address

    def getAddress(self, address):
        return self.address

    def setAge(self, age):
        self.age = age

    def getAge(self, age):
        return self.age


class Teacher(Person):
    salary = None
    curriculum = None

    def __init__(self, salary, curriculum, name, age, address):
        self.salary = salary
        self.curriculum = curriculum
        super().__init__(name, age, address)

    def setSalary(self, salary):
        self.address = salary

    def getAddress(self, address):
        return self.address

    def setAge(self, age):
        self.age = age

    def getAge(self, age):
        return self.age

    def printCurriculum(self):
        print(self.curriculum)


class Student(Person):
    registration = None
    course = None

    def __init__(self, registration, course, name, age, address):
        self.registration = registration
        self.course = course
        super().__init__(name, age, address)

    def setRegistration(self, registration):
        self.registration = registration

    def getRegistration(self):
        return self.registration

    def setCourse(self, course):
        self.course = course

    def getCourse(self):
        return self.course
