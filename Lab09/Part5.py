try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please, enter a valid INT")
else:
    print(result)