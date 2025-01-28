while True:
    try:
        x = int(input("Enter a number: "))
        print(10 / x)
    except (ValueError, ZeroDivisionError):
        print("Error: Invalid input")