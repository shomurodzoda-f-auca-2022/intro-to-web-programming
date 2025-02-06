try:
    with open("example.txt", "x") as file:
        file.write("This is a new file")
except FileExistsError:
    print("File already exists!")