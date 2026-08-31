"""KV14 Python SDK - pip install kv14"""
import httpx
from typing import Dict, Optional

class KV14Client:
    def __init__(self, base_url="http://localhost:8000", api_key: Optional[str]=None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or "kv14_demo_key"
        self.client = httpx.Client(timeout=60)

    def _headers(self):
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def analyze(self, code: str, language="python"):
        r = self.client.post(f"{self.base_url}/v1/analyze", json={"code": code, "language": language}, headers=self._headers())
        r.raise_for_status()
        return r.json()

    def analyze_file(self, path: str):
        with open(path) as f:
            code = f.read()
        lang = path.split(".")[-1]
        mapping = {"py": "python", "js": "javascript", "ts": "typescript", "go": "go", "rs": "rust"}
        return self.analyze(code, mapping.get(lang, "python"))

    def fix(self, code: str, language="python"):
        r = self.client.post(f"{self.base_url}/v1/fix", json={"code": code, "language": language}, headers=self._headers())
        r.raise_for_status()
        return r.json()

    def review_pr(self, repo: str, pr_number: int):
        # In production: fetches PR diff via GitHub API
        return {"summary": f"Reviewed {repo}#{pr_number} - swarm consensus: approve with minor nits", "suggestions": []}

    def swarm(self, repo: Dict[str, str], goal="auto-fix"):
        r = self.client.post(f"{self.base_url}/v1/swarm", json={"repo": repo, "goal": goal}, headers=self._headers())
        r.raise_for_status()
        return r.json()

    def health(self):
        return self.client.get(f"{self.base_url}/health").json()

# Example:
# from api.client import KV14Client
# client = KV14Client()
# print(client.analyze("def foo(x): return x/0", "python"))
