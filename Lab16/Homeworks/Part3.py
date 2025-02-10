import json, time

data = {
    "name": "Farzon",
    "age": 21,
    "year of study": "Junior",
    "courses": ["Intro to Web Programming", "German Language I"]
}

with open("info.json", "w") as file:
    json.dump(data, file, indent=4)
print("Data has been saved to info.json")

print("Datas is being read...")

time.sleep(3)
with open("info.json", "r") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))