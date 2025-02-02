class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("")

class Student(Person):
    def __init__(self, name, age, yearOfStudy):
        super().__init__(name, age)
        self.yearOfStudy = yearOfStudy

    def displayInfo(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am studying in {self.yearOfStudy} year.")

class Teacher(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def displayInfo(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I have {self.experience} years of experience.")

people = [
            Student("John", 24, "Sophomore"),
            Teacher("Monesy", 43, 13),
            Student("Farzon", 21, "Junior"),
            Teacher("Julian", 21, 1)
        ]

for p in people:
    p.displayInfo()