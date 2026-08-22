"""
Chapter 06 - Coding Agent
Simple task planner.

The goal of this chapter is to teach that coding agents do not directly jump into editing.
They first transform a request into executable steps.
"""


def plan(task: str):
    steps = []

    if "add" in task or "create" in task:
        steps.append("inspect project structure")
        steps.append("find related files")
        steps.append("implement change")
        steps.append("run tests")
    else:
        steps.append("understand user request")
        steps.append("inspect context")
        steps.append("execute solution")

    return steps


if __name__ == "__main__":
    for item in plan("add a weather tool"):
        print("-", item)
