import math
from math import *

x = input("Enter a radian: ")
x = int(x)
x = math.degrees(x) # Convert radian to degree
x = ceil(x)

print(f"Cosine of {x} is {cos(x)} and sine of {x} is {sin(x)}")