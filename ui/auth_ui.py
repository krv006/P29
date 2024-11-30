from models.user import User

class AuthUI:
    session_user = None

    def register(self):
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        success, message = user.register()
        print(message)

    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        user = User(email=email, password=password)
        success, result = user.login()
        if success:
            self.session_user = result
            print(f"Welcome, {self.session_user.firstname}!")
        else:
            print(result)
