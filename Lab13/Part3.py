import re

text = "Hallo, Nia, how are you?"
pattern = r"are"

match = re.search(pattern, text)
print(match.group())

pattern = "Hallo"
firstMatch = re.match(pattern, text)
if firstMatch:
    print(firstMatch.group())
else:
    print("None")