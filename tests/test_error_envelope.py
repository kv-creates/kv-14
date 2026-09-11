from fastapi.testclient import TestClient
from api.app import app
c=TestClient(app, raise_server_exceptions=False)
def test_root():
    assert c.get('/').status_code==200
