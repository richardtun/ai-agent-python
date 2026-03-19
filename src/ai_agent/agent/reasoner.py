import json
import os
from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key="test")

class GPTReasoner:
    def decide(self, user_input):
        prompt = f"""
You are AI agent manage job.

Duty:
- Analyse user's request
- Response JSON with the following format:

{{ 
"action": "add | list | remove | unknown",
"task": "task's content if any",
"index": number if remove
}}

Just response the JSON, no explaination.

User request:
"{user_input}"
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return json.loads(response.choices[0].message.content)

class MockGPTReasoner:
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