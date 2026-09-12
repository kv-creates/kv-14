from fastapi.testclient import TestClient
from api.app import app
c=TestClient(app)
def test_metrics():
    assert 'p95_ms' in c.get('/metrics').json()
