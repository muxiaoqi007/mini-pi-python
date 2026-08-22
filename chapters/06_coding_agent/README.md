# Chapter 06 - Coding Agent 🧑‍💻

## Mission
让 Mini Pi 从会回答问题升级为会修改项目的 Agent。

## New abilities

- read_file
- write_file
- execute_command
- run tests

## Architecture

User Request

↓

Agent Planner

↓

Tools

↓

Code Change

↓

Test

↓

Feedback

## Final Challenge

让 Pi 自动完成：

> 给项目增加一个新的 Python 功能，并运行测试。
