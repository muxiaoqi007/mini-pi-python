from pathlib import Path


def write_file(path: str, content: str) -> str:
    """Write project file."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return f"Written: {path}"
