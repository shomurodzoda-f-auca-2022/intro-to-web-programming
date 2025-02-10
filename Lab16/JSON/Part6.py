import json

data = [
    {"name": "Alice", "age": 35},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 22}
]

with open('users.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)