import json

text = '{"name": "John","age": 22,"city of birth": "New York"'

try:
    datas = json.loads(text)
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")