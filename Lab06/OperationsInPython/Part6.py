x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)       # True, because x and y are pointing to same memory location
print(x is z)       # False, even numbers are same, x and z are have two different memory location

a = [1, 2, 3]
b = [1, 2, 3]
print(x is not y)

fruits = ["apple", "orange", "strawberry", "banana"]
print("banana" in fruits)
print("banana" not in fruits)

vegetables = ["potatoes", "tomatoes", "cabbage"]
print("potatoes" in vegetables)
print("tomatoes" in fruits)