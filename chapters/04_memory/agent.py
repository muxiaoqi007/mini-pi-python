from memory import Memory


class MemoryAgent:
    def __init__(self):
        self.memory = Memory()

    def remember(self, text):
        self.memory.add("user", text)

    def context(self):
        return self.memory.load()


if __name__ == "__main__":
    agent = MemoryAgent()
    agent.remember("我的名字叫 Alice")

    print(agent.context())
