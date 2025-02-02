class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print(f"The {self.name} says miyau miyau!!!")

    def displayKind(self):
        print(f"The type of {self.name} is: {self.color}")

cat1 = Cat("Brian", "black")
cat1.bark()
cat1.displayKind()