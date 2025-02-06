import time

fileName = "data.txt"
appendText = "\nWe will start with learning about the background of the Pythong programming language."

print(f"Additional content is writing to a file...")
time.sleep(3)
with open(fileName, "a") as file:
    file.write(appendText)
print(f"Additional content is successfully written to: {fileName}\n")

print(f"Content is reading from the file...")
time.sleep(3)
with open(fileName, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

print(f"Content is successfully read from: {fileName}")
print("\nGoodbye!")