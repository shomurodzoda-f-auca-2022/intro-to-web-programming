age = int(input("Enter your age: "))
key = input("Enter your key word to pass: ").lower()
if age >= 18 and key == "dog":
    print("Access granted!")
elif key != "dog":
    print("The key is wrong, access denied!")
else:
    print("Access denied!")