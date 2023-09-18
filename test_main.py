from fastapi.testclient import TestClient
from fastapi import status
from main import app


client = TestClient(app=app)

def test_correct_country_correct_season():

    response = client.get('/api/recommendations?country=canada&season=winter')

    assert response.status_code == status.HTTP_200_OK

def test_correct_country_wrong_season():
    response = client.get('/api/recommendations?country=canada&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": ['Wrong Season selected, Please select season from Summer, Winter, Spring, Autumn']}
def test_wrong_country_correct_season():
    response = client.get('/api/recommendations?country=canadaa&season=spring')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": ["Wrong Country or City name selected, Please select Valid Country or City"]}

def test_wrong_country_wrong_season():
    response = client.get('/api/recommendations?country=canadaa&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": ["Wrong Country or City name selected, Please select Valid Country or City",
                                                 'Wrong Season selected, Please select season from Summer, Winter, Spring, Autumn']}

