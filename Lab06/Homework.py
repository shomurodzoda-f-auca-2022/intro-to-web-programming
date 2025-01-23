# 1st part of Homework
a = int(input("Enter a whole number: "))
b = float(input("Enter a floating number: "))
c = str(input("Enter a string: "))

print(a, type(a)), print(b, type(b)), print(c, type(c))

# 2nd part of Homework
d = input("Enter a number: ")
print(d, type(d))
d = int(d)
print(d, type(d))
d = float(d)
print(d, type(d))

people = {
    "name": "Farzon",
    "age": 32,
    "job": "Programmer",
}
print(f"Hello, my name is {people['name']}. I am {people['age']} years old and working as a {people['job']}. "
      f"Thanks!")

# 3rd part of Homework
numbers = {1, 3, 4}
print(numbers)
numbers.add(35)
print(numbers)
numbers.remove(1)
print(numbers)
print(35 in numbers)