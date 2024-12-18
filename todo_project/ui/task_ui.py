from todo_project.models.task import Task

class TaskUI:
    def __init__(self, user):
        self.user = user

    def manage_tasks(self):
        while True:
            menu = """
            1) Add Task
            2) List Tasks
            3) Edit Task
            4) Delete Task
            5) Mark Task as Completed
            0) Back
            >>> """
            choice = input(menu).strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_completed()
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.")

    def add_task(self):
        title = input("Task Title: ").strip()
        description = input("Task Description: ").strip()
        task = Task(id=len(Task.load_from_file()) + 1, title=title, description=description)
        task.save()
        print("Task added successfully!")

    def list_tasks(self):
        tasks = Task.load_from_file()
        if tasks:
            for task in tasks:
                status = "Completed" if task.is_completed else "Pending"
                print(f"{task.id}) {task.title} - {status}")
        else:
            print("No tasks available.")

    def edit_task(self):
        task_id = int(input("Enter Task ID to edit: ").strip())
        tasks = Task.load_from_file()
        task_to_edit = next((task for task in tasks if task.id == task_id), None)

        if task_to_edit:
            title = input(f"New title (current: {task_to_edit.title}): ").strip() or task_to_edit.title
            description = input(f"New description (current: {task_to_edit.description}): ").strip() or task_to_edit.description
            task_to_edit.update(title=title, description=description)
            print("Task updated successfully!")
        else:
            print("Task not found!")

    def delete_task(self):
        task_id = int(input("Enter Task ID to delete: ").strip())
        tasks = Task.load_from_file()
        task_to_delete = next((task for task in tasks if task.id == task_id), None)

        if task_to_delete:
            task_to_delete.delete()
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    def mark_task_completed(self):
        task_id = int(input("Enter Task ID to mark as completed: ").strip())
        tasks = Task.load_from_file()
        task_to_complete = next((task for task in tasks if task.id == task_id), None)

        if task_to_complete:
            task_to_complete.is_completed = True
            task_to_complete.save()
            print("Task marked as completed!")
        else:
            print("Task not found!")
