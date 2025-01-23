def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5, 6))

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Farzon", age="21", location="Chicago IL")