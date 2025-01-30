from math import factorial

try:
    x = int(input("Enter a number to factorize: "))
    print(f"Factorial of {x} is {factorial(x)}")
except ValueError:
    print("Negative numbers are not factorized.")

