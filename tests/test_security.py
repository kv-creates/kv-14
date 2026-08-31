"""Security tests"""
from model.security.auditor import scan_code

def test_injection():
    findings = scan_code("eval(user_input)")
    assert len(findings) > 0
    assert findings[0]["owasp"] == "A03_Injection"

def test_clean():
    findings = scan_code("def add(a,b): return a+b")
    assert len(findings) == 0
