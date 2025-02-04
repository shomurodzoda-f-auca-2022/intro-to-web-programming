import re

text = "I study in Portugal, and I myself am from Santos Brazil"
patter = r"Santos"

match = re.search(patter, text)
if match:
    print("Found:", match.group())
else:
    print("No match")