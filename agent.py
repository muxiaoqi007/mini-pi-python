import json
from typing import Any, Dict, List, Optional

from openai import OpenAI

from tools import FUNCTIONS, TOOL_SCHEMAS


class MiniPiAgent:
    """A small, synchronous Pi-style tool loop using Chat Completions."""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        client: Optional[OpenAI] = None,
    ) -> None:
        self.client = client or OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.messages: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "你是一个谨慎的编程助手。先理解问题，再使用工具。"
                    "不要猜测文件内容；需要时调用工具。"
                ),
            }
        ]

    def run(self, user_text: str, max_steps: int = 8) -> str:
        self.messages.append({"role": "user", "content": user_text})

        for _ in range(max_steps):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto",
            )
            assistant = response.choices[0].message
            self.messages.append(assistant.model_dump(exclude_none=True))

            if not assistant.tool_calls:
                return assistant.content or ""

            for call in assistant.tool_calls:
                name = call.function.name
                try:
                    args = json.loads(call.function.arguments or "{}")
                    if name not in FUNCTIONS:
                        raise ValueError(f"未知工具: {name}")
                    result = FUNCTIONS[name](**args)
                except Exception as exc:  # Tool failures become model-visible results.
                    result = f"工具执行失败: {type(exc).__name__}: {exc}"

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": str(result),
                    }
                )

        return "达到最大步骤数，已停止。请把任务拆小后重试。"

