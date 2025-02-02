class Calculator:
    def __init__(self, a):
        self.a = a

    def add(self, b):
        self.a += b

    def getValue(self):
        return self.a

calc = Calculator(5)
print(calc.getValue())
calc.add(7)
print(calc.getValue())