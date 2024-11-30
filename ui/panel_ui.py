from models.category import Category
from ui.task_ui import TaskUI

class PanelUI:
    def __init__(self, user):
        self.user = user

    def manage(self):
        while True:
            menu = """
            1) Manage Categories
            2) Manage Tasks
            3) Log Out
            0) Exit
            >>> """
            choice = input(menu).strip()

            if choice == "1":
                self.manage_categories()
            elif choice == "2":
                self.manage_tasks()
            elif choice == "3":
                self.logout()
            elif choice == "0":
                exit()
            else:
                print("Invalid choice, please try again.")

    def manage_categories(self):
        while True:
            menu = """
            1) Search Categories
            2) Add Category
            3) List Categories
            0) Back
            >>> """
            choice = input(menu).strip()
            if choice == "1":
                search = input("Search: ").strip().lower()
                try:
                    categories = Category.load_from_file()
                    results = [cat for cat in categories if search in cat.name.lower()]
                    if results:
                        for cat in results:
                            print(f"{cat.id}) {cat.name}")
                    else:
                        print("Siz qidirgan kategoriya topilmadi.")
                except Exception as e:
                    print(f"An error occurred while searching categories: {e}")
            elif choice == "2":
                name = input("Category Name: ").strip()
                try:
                    new_category = Category(name=name)
                    new_category.save()
                    print("Category added!")
                except Exception as e:
                    print(f"An error occurred while adding the category: {e}")
            elif choice == "3":
                try:
                    categories = Category.load_from_file()
                    if categories:
                        for cat in categories:
                            print(f"{cat.id}) {cat.name}")
                    else:
                        print("No categories to list.")
                except Exception as e:
                    print(f"An error occurred while listing categories: {e}")
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.")

    def manage_tasks(self):
        task_ui = TaskUI(self.user)
        task_ui.manage_tasks()

    def logout(self):
        print(f"Goodbye, {self.user.firstname}!")
        exit()
