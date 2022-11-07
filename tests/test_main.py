from app.main import app
from app.profile_handler import get_image_url
from fastapi.testclient import TestClient


client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'fastapi-github-evaluator, access /docs for documentation, /evaluation/{user} to single evaluation and /group-evaluation for simultaneous evaluation'}


def test_single_valid_evaluation():
    response = client.get("/evaluation/felipmartins")
    assert response.status_code == 200
    assert len(response.json()) == 17


def test_single_invalid_evaluation():
    response = client.get("/evaluation/akjsdnaljsbhfljkashfjashd")
    assert response.status_code == 200
    assert len(response.json()) == 19


def test_group_evaluation():
    response = client.get('/group-evaluation?user=felipmartins&user=vbuxbaum&user=ipfalvim')
    assert response.status_code == 200
    assert len(response.json()) == 3
