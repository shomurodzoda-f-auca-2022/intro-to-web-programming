import csv

newData = [
    ["David", "35", "Spain"],
    ["Ali", "28", "United Arab Emirates"],
]

with open("data.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(newData)