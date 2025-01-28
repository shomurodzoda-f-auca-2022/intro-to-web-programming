def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(100, 100)
except Exception as e:
    print("Error:", e)
else:
    print("Withdraw successful!")