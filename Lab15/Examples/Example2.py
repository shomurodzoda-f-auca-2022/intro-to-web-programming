import csv, time

fileName = "data.csv"
data = [
    ["Name","Age","Email","City"],
    ["John", "30", "john@example.com", "New York"],
    ["Jane", "25", "jane@example.com", "Los Angeles"],
    ["Alex", "22", "alex@example.com", "Chicago"],
    ["Maria", "28", "maria@example.com", "Miami"],
    ["Tom", "35", "tom@example.com", "Seattle"],
    ["Lucy", "26", "lucy@example.com", "Boston"],
    ["Sam", "40", "sam@example.com", "San Francisco"]
]

print("Writing to a csv file...")
time.sleep(3)
with open(fileName, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Content is successfully written to: {fileName}\n")

print("Reading from a csv file...")
time.sleep(3)
with open(fileName, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']} city.")

print("\nDone!")