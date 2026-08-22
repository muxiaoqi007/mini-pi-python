from planner import plan


def test_plan_create_task():
    result = plan("create a calculator tool")

    assert "inspect project structure" in result
    assert "run tests" in result


if __name__ == "__main__":
    test_plan_create_task()
    print("Coding Agent planner test passed")
