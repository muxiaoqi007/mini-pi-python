# Chapter 04 - Memory 🧠

## Story

你的 Pi 已经会思考，也会调用工具。

但是关闭程序后，它忘记了一切。

这一章为 Pi 安装记忆模块。

## Goals

完成后 Pi 可以：

- 保存历史对话
- 恢复上下文
- 理解短期记忆和长期记忆

## Evolution

Level 1:

```
messages
   |
   v
memory.json
```

Level 2:

```
Agent
 |
SQLite Memory
 |
conversation table
```

Level 3:

```
short memory
+
long memory
+
retrieval
```

## Challenge

第一次运行：

```
我的名字叫 Alice
```

重新启动：

```
我叫什么？
```

Pi 应该回答：

```
你的名字叫 Alice
```

## Unlock

🏆 Memory Keeper
