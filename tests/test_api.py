"""Tests for KV-14 API and swarm"""
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["model"] == "KV-14"

def test_analyze_clean():
    r = client.post("/v1/analyze", json={"code": "def add(a,b): return a+b", "language": "python"})
    assert r.status_code == 200
    assert r.json()["risk_score"] < 50

def test_analyze_buggy():
    r = client.post("/v1/analyze", json={"code": "def foo(x): return x/0", "language": "python"})
    assert r.status_code == 200
    assert r.json()["risk_score"] > 75
    assert len(r.json()["bugs"]) > 0

def test_fix():
    r = client.post("/v1/fix", json={"code": "def foo(x): return x/0", "language": "python"})
    assert r.status_code == 200
    assert "diff" in r.json()

def test_review():
    r = client.post("/v1/review", json={"code": "def add(a,b): return a+b", "language": "python"})
    assert r.status_code == 200
    assert "score" in r.json()

def test_swarm():
    r = client.post("/v1/swarm", json={"repo": {"app.py": "def foo(x): return x/0"}, "goal": "fix"})
    assert r.status_code == 200
    assert "agents" in r.json()

def test_security():
    r = client.post("/v1/security", json={"code": "eval(user_input)", "language": "python"})
    assert r.status_code == 200
    assert "owasp" in r.json()

def test_modernize():
    r = client.post("/v1/modernize", json={"code": "print hello", "source": "python2", "target": "python3"})
    assert r.status_code == 200
    assert r.json()["behavior_preserved"] == 0.97

def test_test_gen():
    r = client.post("/v1/test-gen", json={"code": "def add(a,b): return a+b", "language": "python"})
    assert r.status_code == 200
    assert "tests" in r.json()
