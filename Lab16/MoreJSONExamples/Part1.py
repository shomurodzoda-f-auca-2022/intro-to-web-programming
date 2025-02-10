import json

data = {
    "name": "Bobby",
    "age": 22,
    "courses": ["Math", "English", "Science"]
}

json_data = json.dumps(data, indent=4)
print("Serialization: ")
print(json_data)