while True:
    string = input("Enter a word: ")
    if string == "exit":
        break
    for i in range(len(string)):
        if i % 2 == 0:
            continue
        print(string[i])