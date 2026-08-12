from pathlib import Path
from typing import Callable, Dict
import json


WORKSPACE = Path.cwd().resolve()


def safe_path(relative_path: str) -> Path:
    """Resolve a user-supplied path without allowing workspace escape."""
    target = (WORKSPACE / relative_path).resolve()
    if target != WORKSPACE and WORKSPACE not in target.parents:
        raise ValueError("路径越出了工作目录")
    return target


def read_file(path: str) -> str:
    target = safe_path(path)
    if not target.is_file():
        raise FileNotFoundError(f"文件不存在: {path}")
    return target.read_text(encoding="utf-8")[:20_000]


def list_files(path: str = ".") -> str:
    target = safe_path(path)
    if not target.is_dir():
        raise NotADirectoryError(f"目录不存在: {path}")
    files = [
        str(item.relative_to(WORKSPACE))
        for item in target.iterdir()
        if not item.name.startswith(".")
    ]
    return json.dumps(sorted(files), ensure_ascii=False)


FUNCTIONS: Dict[str, Callable[..., str]] = {
    "read_file": read_file,
    "list_files": list_files,
}


TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "读取工作目录内的文本文件；需要文件内容时必须使用此工具，不要猜测",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "工作目录内的相对路径"}
                },
                "required": ["path"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "列出工作目录或其子目录中的文件",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "相对目录，默认为当前目录", "default": "."}
                },
                "additionalProperties": False,
            },
        },
    },
]

