import time

fileName = "example.txt"
content = "Hello, World!\nWelcome to Python!"

print(f"Content is writing to a file...")
time.sleep(3)
with open(fileName, "w") as file:
    file.write(content)
print(f"Content is successfully written to: {fileName}\n")

print(f"Content is reading from the file...")
time.sleep(3)

with open(fileName, "r") as file:
    content = file.read()
print(content)
print(f"Content is successfully read from: {fileName}")
print("\nGoodbye!")