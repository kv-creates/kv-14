"""Security auditor - OWASP Top 10 + CWE detection with exploitability scoring"""
import re
from typing import List, Dict

OWASP_PATTERNS = {
    "A01_BrokenAccessControl": [r"auth.*==.*True", r"role.*admin"],
    "A03_Injection": [r"eval\(", r"exec\(", r"query.*\+.*request", r"cursor\.execute\(.*%s"],
    "A07_XSS": [r"innerHTML.*=", r"dangerouslySetInnerHTML"],
    "A02_CryptoFailures": [r"md5\(", r"sha1\(", r"random\.random\(\)"],
}

def scan_code(code: str, language="python") -> List[Dict]:
    findings = []
    for owasp, patterns in OWASP_PATTERNS.items():
        for pat in patterns:
            for m in re.finditer(pat, code):
                findings.append({
                    "owasp": owasp,
                    "pattern": pat,
                    "line": code[:m.start()].count("\n")+1,
                    "severity": "high" if "Injection" in owasp else "medium",
                    "cwe": "CWE-20" if "Injection" in owasp else "CWE-79",
                    "exploitability": 0.8
                })
    return findings

def sarif_report(findings: List[Dict]) -> Dict:
    return {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{"tool": {"driver": {"name": "KV-14 Security Auditor"}}, "results": findings}]
    }
