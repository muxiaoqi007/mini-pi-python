"""Chapter 04: simple memory storage.

The goal is teaching, not production usage.
"""

import json
from pathlib import Path


class Memory:
    def __init__(self, path="memory.json"):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, messages):
        self.path.write_text(
            json.dumps(messages, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, role, content):
        messages = self.load()
        messages.append({"role": role, "content": content})
        self.save(messages)
        return messages
