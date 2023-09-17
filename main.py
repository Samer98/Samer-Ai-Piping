from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from helper_functions import chatGPT_response, country_and_season_validation , openAi_key_validation
from country_cities import country_and_cities, seasons
import os
import openai


# Api key for openAI
openai.api_key = os.getenv("openai_key")

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
    data = {}
    data['country_and_cities'] = country_and_cities
    context = {'request': request, "data": data}
    return templates.TemplateResponse("recommendations.html", context)


@app.get("/recommendations", status_code=200)
def get_recommendations(request: Request, country: str, season: str,response: Response):
    data = {}
    season = season.lower()
    country = country.lower()
    country_and_cities.sort()


    openAi_key = openAi_key_validation(openai)
    if openAi_key:
        context = {'request': request, "error_message": openAi_key, "data": data}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return templates.TemplateResponse("recommendations.html", context)

    country_and_season_valid = country_and_season_validation(country, season)
    if country_and_season_valid:
        response.status_code = status.HTTP_400_BAD_REQUEST
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message": country_and_season_valid, "data": data , "loader":False}
        return templates.TemplateResponse("recommendations.html", context)

    try:
        context = chatGPT_response(country, season)

        data['country'] = country
        data['season'] = season
        data['recommendations'] = context['recommendations']
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "data": data}

    except Exception as error_message:
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message": error_message, "data": data}

    return templates.TemplateResponse("recommendations.html", context)




@app.get("/api/recommendations", status_code=200)
def get_recommendations(country: str, season: str,response: Response):
    season = season.lower()
    country = country.lower()
    country_and_cities.sort()

    openAi_key = openAi_key_validation(openai)
    if openAi_key:
        context = {"error_message": openAi_key}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return context

    country_and_season_valid = country_and_season_validation(country, season)
    if country_and_season_valid:
        context = {"error_message": country_and_season_valid}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return context

    try:
        context = chatGPT_response(country, season)
    except Exception as error_message:
        context = {"error_message": error_message}

    return context
