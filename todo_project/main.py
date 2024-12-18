from ui.auth_ui import AuthUI
from ui.panel_ui import PanelUI
from ui.settings_ui import SettingsUI
from ui.task_ui import TaskUI


def main():
    auth = AuthUI()
    while True:
        menu = """
        1) Register
        2) Login
        3) Exit
        >>> """
        choice = input(menu).strip()
        if choice == "1":
            auth.register()
        elif choice == "2":
            auth.login()
            if auth.session_user:
                panel(auth.session_user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def panel(user):
    panel_ui = PanelUI(user)
    settings_ui = SettingsUI(user)
    while True:
        menu = """
        1) Panel
        2) Settings
        3) Tasks
        4) Log out
        >>> """
        choice = input(menu).strip()
        if choice == "1":
            panel_ui.manage_categories()
        elif choice == "2":
            settings_ui.settings()
        elif choice == "3":
            task_ui = TaskUI(user)
            task_ui.manage_tasks()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
