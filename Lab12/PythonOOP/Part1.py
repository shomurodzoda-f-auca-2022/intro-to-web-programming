class Professor:
    def __init__(self, Name, Age, Experience):
        self.Name = Name
        self.Age = int(Age)
        self.Experience = int(Experience)

    def display(self):
        print(f"Hello, My name is {self.Name}, and I am {self.Age} years old. I have {self.Experience} experience.")

professors = [  Professor("Jim", 23, 3),
                Professor("Michael", 30, 8) ]

for professor in professors:
    professor.display()