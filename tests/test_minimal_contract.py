from fastapi.testclient import TestClient
from api.app import app
c=TestClient(app)
def test_health():
    assert c.get('/health').status_code==200
def test_version():
    assert c.get('/version').status_code==200
