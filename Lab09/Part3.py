while True:
    try:
        x = int(input("Enter a number: "))
        print(x)
    except ValueError:
        print("Please enter a valid INT.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")