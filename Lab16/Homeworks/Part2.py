import json

jsonData = '''
    {    
    "name": "Farzon",
    "age": 21,
    "courses": ["Intro to Web Programming", "German Language I"]
    }
'''

jsonData = json.loads(jsonData)
print(jsonData)