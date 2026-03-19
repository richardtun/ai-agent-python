class Actions:
    def __init__(self, memory):
        self.memory = memory

    def add(self, task):
        self.memory.add(task)
        return f"✅ Added task: {task}"

    def all(self):
        tasks = self.memory.all()
        if not tasks:
            return "📭 No task available"
        return "\n".join(
            f"{i + 1}. {task}" for i, task in enumerate(tasks)
        )

    def remove(self, index):
        self.memory.remove(index)
        return "🗑️ Removed task"