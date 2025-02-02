class Phone:
    def __init__(self, brand, price, currency):
        self.brand = brand
        self.price = int(price)
        self.currency = currency

    def display(self):
        print(f"The brand of the phone is {self.brand} and the price is {self.price} in {self.currency}.")

phones = [
        Phone("samsung", 1000, "dollar"),
        Phone("iphone", 87000, "som")
    ]

for phone in phones:
    phone.display()
    print()
