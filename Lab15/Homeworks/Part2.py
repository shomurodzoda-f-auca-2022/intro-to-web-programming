import csv, time

fileName = "info.csv"
data = [
    ["Name", "Age", "City"],
    ["Sultan", "37", "Bishkek"],
    ["Adilet", "40", "Osh"],
    ["Aziret", "25", "Talas"],
]

print(f"Content is writing to a file...")
time.sleep(3)
with open(fileName, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Content is successfully written to: {fileName}\n")

print(f"Content is reading from the file: {fileName}")
with open(fileName, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        time.sleep(1)
        print(row)

time.sleep(1)
print("\nGoodbye!")