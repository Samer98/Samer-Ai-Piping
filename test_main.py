from fastapi.testclient import TestClient
from fastapi import status
from main import app


client = TestClient(app=app)

def test_correct_country_correct_season():

    response = client.get('/recommendations?country=canada&season=winter')

    assert response.status_code == status.HTTP_200_OK

def test_correct_country_wrong_season():
    response = client.get('/recommendations?country=canada&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail":{"error_message": "Error occurred in season name, Please select season from ['summer', 'winter', 'spring', 'autumn'] "}}
def test_wrong_country_correct_season():
    response = client.get('/recommendations?country=canadaa&season=spring')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail":{"error_message": "Error occurred in country or city name, Please select Country or City from this link: "
                          "127.0.0.1.3000/country_cities"}}

def test_wrong_country_wrong_season():
    response = client.get('/recommendations?country=canadaa&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST

