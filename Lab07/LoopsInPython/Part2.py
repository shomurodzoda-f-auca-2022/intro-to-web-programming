age = int(input("Enter your age: "))
while age > 18:
    print("You are older than 18.")
    age = int(input("Enter your age: "))

print("Oops, you are not older than 18.")

age = int(input("Enter your once again age: "))
while True:
    if age < 18:
        print("Oops, you are not older than 18.")
        break

    print("You are older than 18.")
    age = int(input("Enter your age: "))