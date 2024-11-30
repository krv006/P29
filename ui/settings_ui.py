class SettingsUI:
    def __init__(self, user):
        self.user = user

    def settings(self):
        while True:
            menu = """
            1) Edit Full Name
            2) Edit Email
            3) Edit Password
            4) Delete Account
            0) Back
            >>> """
            choice = input(menu).strip()
            if choice == "1":
                self.user.firstname = input("New First Name: ").strip()
                self.user.lastname = input("New Last Name: ").strip()
                self.user.save_to_file()
                print("Name updated and saved!")
            elif choice == "2":
                self.user.email = input("New Email: ").strip()
                self.user.save_to_file()
                print("Email updated and saved!")
            elif choice == "3":
                from getpass import getpass
                self.user.password = getpass("New Password: ").strip()
                self.user.save_to_file()
                print("Password updated and saved!")
            elif choice == "4":
                confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.user.delete_account()
                    print("Account deleted!")
                    break
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.")
