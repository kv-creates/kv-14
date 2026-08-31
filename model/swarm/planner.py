"""Planner agent"""
class PlannerAgent:
    def __init__(self, engine, memory):
        self.engine = engine
        self.memory = memory

    def plan(self, goal: str) -> str:
        files = list(self.memory.repo.keys())
        return f"Plan for goal={goal}: 1) Analyze {len(files)} files 2) Rank risks 3) Fix top 3 bugs 4) Generate tests 5) Review."
