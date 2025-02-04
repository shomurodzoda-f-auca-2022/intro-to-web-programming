import re

text = "My phone number is 5555555 and my office number is 123456789"
pattern = r"\d+"
replacement = "NUMBER"

print(text)
print(re.sub(pattern, replacement, text))