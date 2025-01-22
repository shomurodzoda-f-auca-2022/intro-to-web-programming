greeting = "Hello,"
name = "Farzon"
greeting = greeting + " " + name + "!"      # Concatenation of strings
print(greeting, type(greeting))

fruit = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]
mixed = [1, "apple", 3.14, True]            # List of mixed data types
altogether = fruit + numbers + mixed
print(altogether[len(altogether) - 1], type(altogether[len(altogether) - 1]))
print(altogether, type(altogether))

# Change the element of array
print(fruit[0])
fruit[0] = "grape"
print(fruit[0])

coordinates = (3.8, 4.8)                    # Tuple data types, once initialized cannot be changed or deleted
colors = ("red", "green", "blue")
print(colors, type(colors), coordinates, type(coordinates))