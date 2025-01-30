from math import sqrt as root

x = int(input("Enter a number to find its root: "))
if x < 0:
    x *= -1
print(f"Root of {x} is {root(x)}")