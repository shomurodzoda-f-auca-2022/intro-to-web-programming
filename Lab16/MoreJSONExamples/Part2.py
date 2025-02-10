import json

json_string = '''
{
    "name": "Frank",
    "age": 22,
    "occupation": "Software Engineer"
    }
'''

data = json.loads(json_string)
print("Deserialization: ")
print(json.dumps(data, indent=4))