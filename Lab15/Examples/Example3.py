import time

fileName = "example.txt"
addContent = "\nHave a good learning process!"

print("Content is appending to an existing file...")
time.sleep(3)
with open(fileName, "a") as file:
    file.write(addContent)
print(f"Content is successfully appended to: {fileName}\n")

print("Reading an updated file...")
time.sleep(3)
with open(fileName, "r") as file:
    content = file.read()
    print(content)
print(f"Content is successfully read from updated file: {fileName}\n")

print("Done!")