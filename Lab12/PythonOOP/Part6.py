class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("John", "<PASSWORD>")
print(user1.username)

del user1.username
# print(user1.username) cannot be done as attributes is deleted.
del user1
# user1 object is deleted.