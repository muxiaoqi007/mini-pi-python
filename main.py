import os

from dotenv import load_dotenv

from agent import MiniPiAgent


def create_agent() -> MiniPiAgent:
    load_dotenv()
    return MiniPiAgent(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    )


def main() -> None:
    agent = create_agent()
    print("Mini Pi 已启动。输入 exit 退出。")
    while True:
        prompt = input("\n你 > ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        if not prompt:
            continue
        print("\nAgent >", agent.run(prompt))


if __name__ == "__main__":
    main()

