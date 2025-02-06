import csv
data = [
    ["Name", "Age", "Country"],
    ["Lebron", "37", "United States of America"],
    ["Mikhail", "40", "Russia"],
    ["Farzon", "25", "Tajikistan"],
    ["Thomas", "55", "Germany"]
]

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)