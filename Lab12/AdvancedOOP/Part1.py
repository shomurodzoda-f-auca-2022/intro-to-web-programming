class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = int(balance)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.__owner}. New balance: {self.__balance}.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} from {self.__owner}. Remaining balance: {self.__balance}.")
        else:
            print("Insufficient balance")

    def getBalance(self):
        return self.__balance
    def getOwner(self):
        return self.__owner

account = BankAccount("Farzon", 25000)
account.deposit(5000)
account.withdraw(3000)

print(f"The {account.getOwner()}'s balance is {account.getBalance()}.")