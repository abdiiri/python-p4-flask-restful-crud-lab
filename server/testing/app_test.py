import pytest
from app import app

@pytest.fixture
def test_app():
    app.config.update({
        "TESTING": True,
    })
    yield app

def test_example(test_app):
    client = test_app.test_client()
    response = client.get('/')
    assert response.status_code == 200
