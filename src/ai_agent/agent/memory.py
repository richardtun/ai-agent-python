class Memory:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def all(self):
        return self.tasks