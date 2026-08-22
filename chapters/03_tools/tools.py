"""
Chapter 03

First Tool System

Pi learns to interact with the outside world.
"""

from pathlib import Path


ROOT = Path(__file__).parent


def list_files(path: str = "."):
    """List files in directory."""
    target = (ROOT / path).resolve()

    if not str(target).startswith(str(ROOT.resolve())):
        raise ValueError("path escape blocked")

    return [p.name for p in target.iterdir()]


def read_file(filename: str):
    """Read text file."""
    target = (ROOT / filename).resolve()

    if not str(target).startswith(str(ROOT.resolve())):
        raise ValueError("path escape blocked")

    return target.read_text(encoding="utf-8")


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
}
