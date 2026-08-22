from pathlib import Path


class SkillLoader:
    def __init__(self, skill_dir="skills"):
        self.skill_dir = Path(skill_dir)

    def load(self, name):
        path = self.skill_dir / f"{name}.md"

        if not path.exists():
            return None

        return path.read_text(encoding="utf-8")

    def list_skills(self):
        if not self.skill_dir.exists():
            return []

        return [
            p.stem
            for p in self.skill_dir.glob("*.md")
        ]
