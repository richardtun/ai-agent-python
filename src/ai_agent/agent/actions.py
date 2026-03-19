class Actions:
    def __init__(self, memory):
        self.memory = memory

    def add_task(self, task):
        self.memory.add_task(task)
        return f"✅ Added task: {task}"

    def list_tasks(self):
        tasks = self.memory.list_tasks()
        if not tasks:
            return "📭 No task available"
        return "\n".join(
            f"{i + 1}. {task}" for i, task in enumerate(tasks)
        )

    def remove_task(self, index):
        self.memory.remove_task(index)
        return "🗑️ Removed task"