from ai_agent.logger import logger
from ai_agent.agent.memory import Memory
from ai_agent.agent.actions import Actions
from ai_agent.agent.reasoner import GPTReasoner, MockGPTReasoner

class AIAgent:
    def __init__(self):
        self.memory = Memory()
        self.actions = Actions(self.memory)
        # self.reasoner = GPTReasoner()
        
        self.primary_reasoner = GPTReasoner()
        self.fallback_reasoner = MockGPTReasoner()


    def run(self, user_input):
        logger.debug(f"User input: {user_input}")

        try:
            logger.info("Using GPT reasoner")
            decision = self.primary_reasoner.decide(user_input)
            # print("🧠 GPT Reasoner used")

        except Exception as e:
            logger.warning("GPT failed, switching to Mock GPT")
            logger.debug(f"GPT error detail: {e}")

            # print("⚠️ GPT error, switching to Mock GPT")
            # print("Reason:", str(e))

            decision = self.fallback_reasoner.decide(user_input)

        # decision = self.reasoner.decide(user_input)

        logger.debug(f"Decision received: {decision}")

        action = decision.get("action")


        if action == "add":
            logger.info("Action: ADD task")
            return self.actions.add_task(decision.get("task"))

        elif action == "list":
            logger.info("Action: LIST tasks")
            return self.actions.list_tasks()

        elif action == "remove":
            try:
                index = decision.get("index", 1) - 1
                logger.info(f"Action: REMOVE task at index {index}")
                return self.actions.remove_task(index)
            except Exception as e:
                logger.error(f"Failed to remove task: {e}")
                return "❌ Cannot remove task"

        else:
            logger.warning("Unknown action requested")
            return "❓ Not understand your request."