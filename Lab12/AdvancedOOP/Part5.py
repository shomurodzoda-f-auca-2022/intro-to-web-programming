class Papa:
    @staticmethod
    def hello():
        print("Hello, Papa")

class Mama:
    @staticmethod
    def hello():
        print("Hello, Mama")

class Child(Papa, Mama):
    @staticmethod
    def hello():
        print("Hello, Child")

print(Papa.hello())
print(Mama.hello())
print(Child.hello())