import json, time

data = {
    "name": "Bobby",
    "age": 22,
    "courses": ["Math", "English", "Science"]
}

with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been created.")

print("Data is being read...")
time.sleep(3)

with open('student.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))