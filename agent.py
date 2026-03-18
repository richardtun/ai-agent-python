# Simple AI Task Agent

# import os
# import json
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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

# class GPTReasoner:
#     def decide(self, user_input):
#         prompt = f"""
# You are AI agent manage job.

# Duty:
# - Analyse user's request
# - Response JSON with the following format:

# {{ 
# "action": "add | list | remove | unknown",
# "task": "task's content if any",
# "index": number if remove
# }}

# Just response the JSON, no explaination.

# User request:
# "{user_input}"
# """

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0
#         )

#         return json.loads(response.choices[0].message.content)

class GPTReasoner:
    """
    Mock GPT Reasoner
    Simulate GPT no need to call API
    """

    def decide(self, user_input):
        text = user_input.lower()

        # add task
        if "add" in text or "let" in text:
            task = (
                user_input
                .replace("add", "")
                .replace("let", "")
                .strip()
            )
            return {
                "action": "add",
                "task": task
            }

        # view list
        if "view" in text or "list" in text:
            return {
                "action": "list"
            }

        # remove task
        if "remove" in text:
            # simple: remove the first task
            return {
                "action": "remove",
                "index": 1
            }

        return {
            "action": "unknown"
        }


class AIAgent:
    def __init__(self):
        self.memory = Memory()
        self.actions = Actions(self.memory)
        self.reasoner = GPTReasoner()

    def run(self, user_input):
        
        decision = self.reasoner.decide(user_input)

        action = decision.get("action")


        if action == "add":
            return self.actions.add_task(decision.get("task"))

        elif action == "list":
            return self.actions.list_tasks()

        elif action == "remove":
            index = decision.get("index", 1) - 1
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