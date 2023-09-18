from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from helper_functions import is_season_present, is_country_present
from country_cities import country_and_cities
from pathlib import Path
from chatGPT import ChatGPT


app = FastAPI()

# For getting the static files in the project
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get("/", status_code=200)
async def home_page(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('home.html', context)


@app.get("/recommendations_page", status_code=200)
async def get_recommendations_page(request: Request):
    country_and_cities.sort()
    data = {'country_and_cities': country_and_cities}
    context = {'request': request, "data": data}
    return templates.TemplateResponse("recommendations.html", context)


@app.get("/api/recommendations", status_code=200)
def get_recommendations(country: str, season: str, response: Response):
    season = season.lower()
    country = country.lower()
    country_and_cities.sort()

    if not ChatGPT.is_key_present():
        raise HTTPException (status_code=404, detail="openai API key is not found")

    error_message = []
    if not is_country_present(country):
        error_message.append("Wrong Country or City name selected, Please select Valid Country or City")

    if not is_season_present(season):
        error_message.append( "Wrong Season selected, Please select season from Summer, Winter, Spring, Autumn")

    if len(error_message) > 0:
        raise HTTPException(status_code=400, detail=error_message)

    try:
        recommendations = ChatGPT.get_travel_recommendations(country, season)
        context = {"country": country, 'season': season, "recommendations": recommendations}
        return context

    except Exception as error_message:

        raise HTTPException(status_code=400,detail=error_message)


@app.get("/recommendations", status_code=200)
def get_recommendations(request: Request, country: str, season: str):
    data = {}
    season = season.lower()
    country = country.lower()
    country_and_cities.sort()

    if not ChatGPT.is_key_present():
        error_message = ["Error occurred in openai API key is not found"]
        context = {'request': request, "error_message": error_message, "data": data}
        return templates.TemplateResponse("recommendations.html", context)

    error_message = []
    if not is_country_present(country):
        error_message.append("Wrong Country or City name selected, Please select Valid Country or City")
    if not is_season_present(season):
        error_message.append("Wrong Season selected, Please select season from Summer, Winter, Spring, Autumn")

    if len(error_message) > 0:
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message":error_message, "data": data}
        return templates.TemplateResponse("recommendations.html", context)

    try:
        recommendations = ChatGPT.get_travel_recommendations(country, season)
        data['country'] = country
        data['season'] = season
        data['recommendations'] = recommendations
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "data": data}

    except Exception as error_message:
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message": error_message, "data": data}

    return templates.TemplateResponse("recommendations.html", context)




