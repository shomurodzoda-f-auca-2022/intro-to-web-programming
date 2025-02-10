import json

data = [
    {"name": "Alice", "age": 35},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 22}
]

jsonData = json.dumps(data, indent=4)
print(jsonData)