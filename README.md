# Mini Pi Python

一个适合初学者阅读的最小 Agent 实现。它保留了 Pi Agent 最核心的工作方式：

1. 把用户消息交给支持 OpenAI Chat Completions 格式的模型。
2. 模型决定直接回答，还是产生 `tool_calls`。
3. Python 执行工具，把结果作为 `role=tool` 消息放回上下文。
4. 重复以上过程，直到模型给出最终答案或达到最大步数。

项目只有两个工具：列出目录和读取文件。代码短小，但包含路径越界防护、工具异常回传和最大循环步数，适合作为复刻 Pi Agent 的起点。

## 目录结构

```text
mini-pi-python/
├── agent.py          # Agent 循环：模型调用、tool_calls、工具结果回填
├── tools.py          # 工具实现、JSON Schema 和路径安全检查
├── main.py           # 可交互命令行入口
├── test_tools.py     # 工具与安全边界测试
├── requirements.txt
└── .env.example
```

## 1. 安装

需要 Python 3.9 或更高版本。

```bash
git clone https://github.com/muxiaoqi007/mini-pi-python.git
cd mini-pi-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell 激活虚拟环境：

```powershell
.venv\Scripts\Activate.ps1
```

## 2. 配置 OpenAI 兼容 API

```bash
cp .env.example .env
```

然后编辑 `.env`：

```dotenv
OPENAI_API_KEY=你的密钥
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini
```

`OPENAI_BASE_URL`、模型名和密钥都可以替换为其他支持 OpenAI Chat Completions 与工具调用格式的服务。不要提交真实 `.env` 或 API 密钥。

## 3. 运行

```bash
python main.py
```

可以尝试：

```text
先列出当前目录，再读取 README.md，并用一句话介绍这个项目。
```

输入 `exit` 或 `quit` 退出。

## 4. 测试

```bash
python -m unittest -v test_tools.py
python -m py_compile agent.py tools.py main.py
```

## 核心循环

重点阅读 `agent.py` 的 `MiniPiAgent.run()`：

```python
for _ in range(max_steps):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOL_SCHEMAS,
        tool_choice="auto",
    )
    assistant = response.choices[0].message

    if not assistant.tool_calls:
        return assistant.content or ""

    for call in assistant.tool_calls:
        result = FUNCTIONS[call.function.name](**arguments)
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": str(result),
        })
```

真正的 Agent 并不是一次模型请求，而是“模型决策 → 执行工具 → 回填结果 → 再次决策”的循环。

## 已验证范围

- OpenAI 兼容的基础对话请求
- `tool_calls` 工具调用协议
- 列目录 → 读文件 → 生成最终回答的多步循环
- 工作目录路径越界拦截
- Python 单元测试和语法编译

不同服务商对工具调用协议的兼容程度不同。如果普通对话成功、工具调用失败，应优先检查服务端是否完整支持 Chat Completions 的 `tools`、`tool_choice` 和 `tool_calls` 字段。

## 下一步可以怎样扩展

1. 增加 `write_file`，并设计写入审批机制。
2. 把消息保存到 JSON 或 SQLite，实现会话恢复。
3. 增加上下文压缩，避免历史消息无限增长。
4. 把工具系统改为可注册的插件结构。
5. 增加流式输出、重试、超时和日志追踪。

## License

[MIT](LICENSE)
