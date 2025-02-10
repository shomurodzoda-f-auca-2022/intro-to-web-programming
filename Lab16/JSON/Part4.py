import json

text = '{"name": "John","age": 22,"city of birth": "New York"}'
data = json.loads(text)

print(data['name'])
print(type(data['age']))