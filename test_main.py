from fastapi.testclient import TestClient
from fastapi import status
from main import app


client = TestClient(app=app)

def test_country_season_correct():

    response = client.get('/recommendations?country=canada&season=winter')

    assert response.status_code == status.HTTP_200_OK

def test_country_wrong_season_correct():
    response = client.get('/recommendations?country=canada&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST