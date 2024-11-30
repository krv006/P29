class Task:
    task_file = "tasks.txt"

    def __init__(self, id, title, description, is_completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed

    def save(self):
        tasks = self.load_from_file()
        tasks.append(self)
        with open(self.task_file, "w") as file:
            for task in tasks:
                file.write(
                    f"{task.id},{task.title},{task.description},{task.is_completed}\n")

    def delete(self):
        tasks = self.load_from_file()
        tasks = [task for task in tasks if task.id != self.id]
        with open(self.task_file, "w") as file:
            for task in tasks:
                file.write(
                    f"{task.id},{task.title},{task.description},{task.is_completed}\n")

    @classmethod
    def load_from_file(cls):
        tasks = []
        try:
            with open(cls.task_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    id, title, description, is_completed = line.strip().split(",")
                    tasks.append(
                        cls(int(id), title, description, is_completed == 'True'))
        except FileNotFoundError:
            return []
        return tasks

    def update(self, title=None, description=None, is_completed=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if is_completed is not None:
            self.is_completed = is_completed
        self.save()
