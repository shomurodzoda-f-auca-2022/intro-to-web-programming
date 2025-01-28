import math

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return math.sqrt(number)

try:
    result = square_root(25)
except NegativeNumberError as e:
    print("Error:", e)
else:
    print("Result:", result)