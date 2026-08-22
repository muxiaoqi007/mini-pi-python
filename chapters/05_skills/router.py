class SkillRouter:
    def __init__(self, skills):
        self.skills = skills

    def route(self, task):
        task = task.lower()

        for skill in self.skills:
            if skill.lower() in task:
                return skill

        if "sql" in task or "database" in task:
            return "sql"

        if "python" in task or "code" in task:
            return "python"

        return None
