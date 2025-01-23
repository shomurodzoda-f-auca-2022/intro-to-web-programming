age = int(input("Enter your age: "))
key = int(input("Enter your key for entering: "))
if age > 17:
    if key == 212:
        print("You can enter the disco club!")
    else:
        print("Wrong key, please leave!")
else:
    print("You are not old enough to enter the disco club!")