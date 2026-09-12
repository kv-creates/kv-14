"""Swarm Orchestrator - 5 agents collaborating via shared memory"""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class SwarmMemory:
    repo: Dict[str, str]
    plan: str = ""
    diffs: List[str] = field(default_factory=list)
    reviews: List[str] = field(default_factory=list)
    security: List[Dict] = field(default_factory=list)
    logs: List[str] = field(default_factory=list)

    def log(self, agent: str, msg: str):
        self.logs.append(f"[{agent}] {msg}")

class SwarmOrchestrator:
    def __init__(self, engine):
        self.engine = engine
        self.memory = None

    def run(self, repo: Dict[str, str], goal="auto-fix"):
        self.memory = SwarmMemory(repo=repo)
        # 1. Planner
        from .planner import PlannerAgent
        planner = PlannerAgent(self.engine, self.memory)
        plan = planner.plan(goal)
        self.memory.log("planner", plan)

        # 2. Coder
        from .executor import CoderAgent
        coder = CoderAgent(self.engine, self.memory)
        diff = coder.execute(plan)

        # 3. Tester
        from .executor import TesterAgent
        tester = TesterAgent(self.engine, self.memory)
        passed = tester.verify(diff)

        # 4. Reviewer
        from .reviewer import ReviewerAgent
        reviewer = ReviewerAgent(self.engine, self.memory)
        review = reviewer.review(diff)

        # 5. Security
        from .reviewer import SecurityAgent
        sec = SecurityAgent(self.engine, self.memory)
        sec_report = sec.scan(repo)

        return {
            "goal": goal,
            "plan": plan,
            "diff": diff,
            "tests_passed": passed,
            "review": review,
            "security": sec_report,
            "logs": self.memory.logs,
            "consensus": "approve" if passed and "LGTM" in review else "request_changes"
        }
# v14.2: shared memory TTL 1h
MEMORY_TTL_S = 3600
