# Task 1
list = [10, 20, 30, 40, 50]
list.append(60)
list.insert(1, 15)
list.remove(30)
list.reverse()
list.sort()
for item in list:
    print(item, end=" ")
print()

print() # Separation of each task

# Task 2
i = 0
while i < 3:
    print(list[i], end=" ")
    i += 1
print()

print(list[len(list) - 1], list[len(list) - 2])
print(list[::-1])

print() # Separation of each task

# Task 3
dictionary = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}
dictionary.update({"subject": "Math"})
dictionary.update({"grade": "A+"})
dictionary.pop("age")

for key, value in dictionary.items():
    print(f"{key}: {value}")

print() # Separation of each task

# Task 4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Task 5
colors = ("red", "blue", "green", "red", "yellow")
print("Index of green is", colors.index("green"))
print(f"Red color appears", colors.count("red"), "times.")

print() # Separation of each task

# Task 6
companyDictionary = {
    "employees": [
        {
            "name": "John",
            "position": "Project Manager",
            "salary": 20000
         },
        {
            "name": "Madam",
            "position": "Manager of Products",
            "salary": 30000
        }
    ]
}

companyDictionary["employees"].append(
    {
        "name": "Frank",
        "position": "Director executive",
        "salary": 70000
    }
)

for employee in companyDictionary["employees"]:
    print(employee["name"])