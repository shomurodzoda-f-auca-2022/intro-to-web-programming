import random

x = random.randint(1, 100)
print("The random number is", x)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

names = ["John", "Mike", "Alex", "Jonathan"]
random.shuffle(names)
chosenName = random.choice(names)
print("The chosen name is:", chosenName)
