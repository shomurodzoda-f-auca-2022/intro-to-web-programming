# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello, my name is {name} and I am {age} years old!")

a, b, c = input("Enter three numbers: ").split()
a, b, c = float(a), float(b), float(c)
total = a + b + c
average = total / 3
product = a * b * c
print(f"The sum, average and product of given numbers are: {total}, {average}, {product}")