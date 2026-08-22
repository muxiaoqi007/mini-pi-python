"""
Chapter 01: Brain

第一个拥有大脑的 Mini Pi。

目标：理解 LLM 调用的最小闭环。
"""

from openai import OpenAI


client = OpenAI()


def ask_llm(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(ask_llm("你好，我是 Mini Pi"))
