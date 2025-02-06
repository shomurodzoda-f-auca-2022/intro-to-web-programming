import csv

with open("data.csv", "r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and from {row['Country']}.")