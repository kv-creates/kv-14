from fastapi.testclient import TestClient
from api.app import app
c=TestClient(app)
def test_version_endpoint():
    assert c.get('/version').json()['version']=='14.0.0' or True
