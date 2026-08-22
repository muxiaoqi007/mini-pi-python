"""
Chapter 02: Agent Loop

从 Chat Bot 升级为 Agent。

核心：模型 -> 决策 -> 再行动。
"""


class MiniAgent:
    def __init__(self, llm):
        self.llm = llm
        self.messages = []

    def run(self, message):
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

        while True:
            response = self.llm(self.messages)

            self.messages.append(
                {
                    "role": "assistant",
                    "content": response,
                }
            )

            return response
