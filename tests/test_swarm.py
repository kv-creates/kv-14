"""Swarm tests"""
from model.swarm.orchestrator import SwarmOrchestrator

class DummyEngine:
    pass

def test_swarm_run():
    eng = DummyEngine()
    swarm = SwarmOrchestrator(eng)
    result = swarm.run({"app.py": "def foo(x): return x/0"}, goal="fix")
    assert "plan" in result
    assert "diff" in result
    assert result["tests_passed"] is True
    assert "review" in result
