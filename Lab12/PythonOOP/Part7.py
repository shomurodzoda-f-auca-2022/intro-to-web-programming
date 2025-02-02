class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return True
        return False

users = [
        User("Johnny", "1223"),
        User("Thomas", "hello"),
        User("Muller", "Bayern")
    ]

while True:
    usernameInput = input("Enter a name verify: ")

    if usernameInput == "exit":
        break
    userNameFound = False
    for user in users:
        if user.username == usernameInput:
            userNameFound = True
            print(f"Username {user.username} is found!")
            passwordInput = input(f"Enter password of {usernameInput} to log in: ")
            if user.login(passwordInput):
                print(f"Welcome, {user.username}!")
                break
            else:
                print("Incorrect password, please try again!")
    if not userNameFound:
        print(f"Username {usernameInput} not found, please try again!")
    print()