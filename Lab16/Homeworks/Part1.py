import json

data = {
    "name": "Farzon",
    "age": 21,
    "courses": ["Intro to Web Programming", "German Language I"]
}

json_data = json.dumps(data, indent=4)
print(json_data)