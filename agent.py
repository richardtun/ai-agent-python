# Simple AI Task Agent

class Memory:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks


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


class Reasoner:
    def decide(self, user_input):
        text = user_input.lower()
        if "add" in text:
            return "add"
        elif "list" in text:
            return "list"
        elif "remove" in text:
            return "remove"
        else:
            return "unknown"


class AIAgent:
    def __init__(self):
        self.memory = Memory()
        self.actions = Actions(self.memory)
        self.reasoner = Reasoner()

    def run(self, user_input):
        action = self.reasoner.decide(user_input)

        if action == "add":
            task = user_input.replace("add", "").strip()
            return self.actions.add_task(task)

        elif action == "list":
            return self.actions.list_tasks()

        elif action == "remove":
            index = int(input("Input task number to remove: ")) - 1
            return self.actions.remove_task(index)

        else:
            return "❓ Not understand your request."


if __name__ == "__main__":
    agent = AIAgent()
    print("🤖 AI Task Agent (input 'exit' to exit)")

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        print("Agent:", agent.run(user_input))