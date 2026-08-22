import subprocess


def execute_command(command: str) -> str:
    """Execute safe shell command."""
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout
