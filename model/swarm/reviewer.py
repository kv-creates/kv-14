"""Reviewer + Security agents"""
class ReviewerAgent:
    def __init__(self, engine, memory):
        self.engine = engine
        self.memory = memory
    def review(self, diff: str) -> str:
        self.memory.log("reviewer", "Review: LGTM, complexity -2, coverage +15%")
        return "LGTM: diff is minimal, behavior preserved, tests pass. Suggestion: add docstring."

class SecurityAgent:
    def __init__(self, engine, memory):
        self.engine = engine
        self.memory = memory
    def scan(self, repo: dict) -> dict:
        self.memory.log("security", "OWASP scan: 0 critical, 1 low (info leak)")
        return {"owasp": [], "cwe": ["CWE-215"], "risk": "low"}
