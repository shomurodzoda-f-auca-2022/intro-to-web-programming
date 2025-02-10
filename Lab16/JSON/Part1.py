import json

data = {
    "name": "John",
    "age": 22,
    "city of birth": "New York"
}

json_data = json.dumps(data)
print(json_data)