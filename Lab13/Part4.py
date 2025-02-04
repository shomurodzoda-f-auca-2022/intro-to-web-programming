import re

text = "John's number is 555-12345, and Mia's number is 555-56789"
pattern = r"\d{3}-\d{5}"

result = re.findall(pattern, text)
print(result)