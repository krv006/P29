import os

users_file = os.path.join("data", "users.txt")


class User:
    def __init__(self, _id=None, firstname=None, lastname=None, email=None, password=None):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def save_to_file(self):
        users = User.load_from_file()
        for idx, user in enumerate(users):
            if user.id == self.id:
                users[idx] = self
                break
        else:
            self.id = users[-1].id + 1 if users else 1
            users.append(self)

        with open(users_file, "w") as file:
            for user in users:
                file.write(f"{user.id},{user.firstname},{user.lastname},{user.email},{user.password}\n")

    @staticmethod
    def load_from_file():
        users = []
        if os.path.exists(users_file):
            with open(users_file, "r") as file:
                for line in file:
                    _id, firstname, lastname, email, password = line.strip().split(",")
                    users.append(User(int(_id), firstname, lastname, email, password))
        return users

    def register(self):
        users = User.load_from_file()
        if any(user.email == self.email for user in users):
            return False, "Email already exists!"
        if len(self.password) < 4:
            return False, "Password is too short!"
        self.id = users[-1].id + 1 if users else 1
        self.save_to_file()
        return True, "Registration successful!"

    def login(self):
        users = User.load_from_file()
        for user in users:
            if user.email == self.email and user.password == self.password:
                return True, user
        return False, "Invalid email or password."

    def delete_account(self):
        users = User.load_from_file()
        users = [user for user in users if user.id != self.id]
        with open(users_file, "w") as file:
            for user in users:
                file.write(f"{user.id},{user.firstname},{user.lastname},{user.email},{user.password}\n")
