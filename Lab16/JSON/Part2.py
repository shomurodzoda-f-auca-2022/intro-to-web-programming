import json

data = {
    "name": "John",
    "age": 22,
    "city of birth": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)