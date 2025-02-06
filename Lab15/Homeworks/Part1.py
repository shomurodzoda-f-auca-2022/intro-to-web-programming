import time

fileName = "data.txt"
lines = ("Good morning, programmers! "
         "Welcome to learning new Programming Language, Python. Python is a famous, worldwide programming language, "
         "easy to learn, strong enough to do various things.")

print(f"Content is writing to a file...")
time.sleep(3)
with open(fileName, "w") as file:
    file.write(lines)
print(f"Content is successfully written to: {fileName}\n")

print(f"Content is reading from the file...")
time.sleep(3)
with open(fileName, "r") as file:
    lines = file.readlines()
    print(lines)

print(f"Content is successfully read from: {fileName}")
print("\nGoodbye!")