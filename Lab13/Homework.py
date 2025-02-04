# Part 1
import re
from re import search

text = "Our office number is 555-1234 and direct phone number is 555-5678. For emergencies, dial 555-9999"
pattern = r"\d{3}-\d{4}"

print("Phone Numbers Found:", re.findall(pattern, text))

print() # separate each lab exercise

# Part 2
text = "Hello, my name is Farzon!"
pattern = r"Hello"

print("Using re.match()...")
match = re.match(pattern, text)
if match:
    print("Match Found:", match.group())
else:
    print("No Match Found!")

print("Using re.search()...")
text = "Why you did not wave me a Hello???"
search = re.search(pattern, text)
if search:
    print("Search Found:", search.group())
else:
    print("No Search Found!")

print() # separate each lab exercise

# Part 3
text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."
pattern = r"\d+"

print(text) # prints the text before replacement

text = re.sub(pattern, "NUMBER", text)
print(text) # prints the text after replacement