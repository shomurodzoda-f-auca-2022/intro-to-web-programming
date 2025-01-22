# We take the input as string(str) initially
a = input("Enter a number: ")
print(a, type(a))

# Convert the input to INT
a = int(a)
print(a, type(a))

# Convert the input to FLOAT
a = float(a)
print(a, type(a))

# We retake the input and convert it to list
a = input("Enter a word: ")
a = list(a)
print(a, type(a))