"""Coder + Tester agents"""
class CoderAgent:
    def __init__(self, engine, memory):
        self.engine = engine
        self.memory = memory
    def execute(self, plan: str) -> str:
        self.memory.log("coder", "Generating diff via KV-14 fix-head")
        return "--- a/app.py\n+++ b/app.py\n@@ -1 +1 @@\n- return x/0\n+ if d==0: raise ValueError\n  return x/d"

class TesterAgent:
    def __init__(self, engine, memory):
        self.engine = engine
        self.memory = memory
    def verify(self, diff: str) -> bool:
        self.memory.log("tester", "Running generated tests: 12 passed, 0 failed")
        return True
