"""
Chapter 03

Simplified Agent with Tool Calling.

Learning version only.
"""

from tools import TOOLS


class ToolAgent:

    def __init__(self, model):
        self.model = model
        self.messages = []

    def run(self, user_input):
        self.messages.append({
            "role": "user",
            "content": user_input,
        })

        while True:
            response = self.model.chat(
                self.messages,
                tools=list(TOOLS.keys())
            )

            if response.get("tool_call"):
                name = response["tool_call"]["name"]
                args = response["tool_call"].get("arguments", {})

                result = TOOLS[name](**args)

                self.messages.append({
                    "role": "tool",
                    "content": str(result)
                })

                continue

            return response["content"]
