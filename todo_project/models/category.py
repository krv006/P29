class Category:
    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def save(self):

        try:
            categories = Category.load_from_file()
            self.id = categories[-1].id + 1 if categories else 1
            with open("data/categories.txt", "a") as file:
                file.write(f"{self.id},{self.name}\n")
        except Exception as e:
            raise RuntimeError(f"Failed to save category: {e}")

    @staticmethod
    def load_from_file():
        categories = []
        try:
            with open("data/categories.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",", 1)
                    if len(parts) == 2:
                        _id, name = parts
                        categories.append(Category(_id=int(_id), name=name))
        except FileNotFoundError:
            return categories
        except Exception as e:
            raise RuntimeError(f"Error loading categories: {e}")
        return categories