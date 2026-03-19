from ai_agent.logger import logger
from ai_agent.agent.agent import AIAgent

def main():
    logger.info("AI Agent started")
    # logger()
    agent = AIAgent()

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        print("Agent:", agent.run(user_input))
    # agent.run()

if __name__ == "__main__":
    main()
