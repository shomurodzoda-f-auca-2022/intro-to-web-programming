import csv

with open("data.csv", "r",newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)