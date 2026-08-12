import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import tools


class ToolTests(unittest.TestCase):
    def test_list_and_read(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "hello.txt").write_text("hello", encoding="utf-8")
            with patch.object(tools, "WORKSPACE", root.resolve()):
                self.assertIn("hello.txt", tools.list_files())
                self.assertEqual(tools.read_file("hello.txt"), "hello")

    def test_workspace_escape_is_blocked(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            with patch.object(tools, "WORKSPACE", root.resolve()):
                with self.assertRaises(ValueError):
                    tools.safe_path("../secret.txt")


if __name__ == "__main__":
    unittest.main()

