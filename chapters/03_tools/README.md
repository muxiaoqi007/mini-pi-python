# Chapter 03 - Give Pi Hands 🛠️

## Story

你的 Pi 已经拥有大脑，也能够循环思考。

但是它只能聊天，无法观察真实世界。

这一章我们给 Pi 安装第一组工具。

## Goal

完成后，你的 Agent 可以：

- 查看目录
- 读取文件
- 根据工具结果继续推理

## Core Concept

Agent = LLM + Loop + Tools

流程：

```
User
 |
LLM
 |
决定调用工具
 |
Python执行
 |
Tool Result
 |
LLM继续思考
```

## Challenge

实现两个工具：

1. list_files
2. read_file

然后让 Agent 完成：

> 找到 README.md 并总结项目

## Unlock

🏆 Tool Master

下一章：Memory
