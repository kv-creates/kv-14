from fastapi.testclient import TestClient
from api.app import app
c=TestClient(app)
def test_batch():
    assert c.post('/v1/batch-analyze', json={'files':{'a.py':'x=1'}}).status_code==200
