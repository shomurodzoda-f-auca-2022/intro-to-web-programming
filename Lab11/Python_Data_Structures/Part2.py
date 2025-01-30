students = {
    "name": "John",
    "age": 22,
    "grade": "A"
}

print(students["age"])  # print the value based on a key

for key, value in students.items():
    print(f"{key} = {value}")

print()

students.update({"name": "Bob"})
students.update({"grade": "C-"})

for key, value in students.items():
    print(f"{key} = {value}")