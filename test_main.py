from fastapi.testclient import TestClient
from fastapi import status
from main import app


client = TestClient(app=app)

def test_country_season_correct():

    response = client.get('/recommendations?country=Canda&season=winter')

    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == {"country":"Canda","season":"winter","recommendations":["1. Skiing and Snowboarding: Hit the slopes at popular ski resorts like Whistler Blackcomb in British Columbia or Banff Sunshine Village in Alberta.","2. Ice Skating: Lace up your skates and glide across frozen lakes or visit outdoor rinks like the Rideau Canal Skateway in Ottawa or Nathan Phillips Square in Toronto.","3. Snowshoeing: Explore Canada's picturesque winter landscapes by strapping on some snowshoes and venturing into national parks or wilderness areas.","4. Dog Sledding: Experience the thrill of mushing your own team of huskies through snowy trails in regions like Yukon or Quebec.","5. Winter Festivals: Enjoy festivities like the Quebec Winter Carnival in Quebec City or Winterlude in Ottawa, featuring ice sculptures, ice slides, live music, and more.","6. Ice Fishing: Join locals and try your hand at ice fishing on frozen lakes and rivers, especially in provinces like Manitoba or Saskatchewan.","7. Northern Lights Viewing: Head to Canada's northern regions, such as Yellowknife or Whitehorse, for a chance to witness the breathtaking Aurora Borealis.","8. Winter Wildlife Tours: Explore national parks like Jasper or Churchill to spot majestic creatures like polar bears, moose, or reindeer in their natural habitat.","9. Hot Springs: Relax in soothing hot springs like the Banff Upper Hot Springs in Alberta or the Peninsula Hot Springs in British Columbia, surrounded by snow-covered landscapes.","10. Winter Hiking: Bundle up and embark on scenic winter hikes in areas like the Canadian Rockies or Cape Breton Highlands National Park, offering stunning winter vistas."]}

def test_country_wrong_season_correct():
    response = client.get('/recommendations?country=Canda&season=springs')

    assert response.status_code == status.HTTP_400_BAD_REQUEST