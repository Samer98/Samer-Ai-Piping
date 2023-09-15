from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import openai
from country_cities import country_and_cities, seasons
from pathlib import Path
from dotenv import load_dotenv
import os


# Function used for getting environment variables
def configure():
    load_dotenv()


configure()

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


@app.get("/recommendations", status_code=201)
def get_recommendations(request: Request, country: str, season: str):
    data = {}
    season = season.lower()
    country = country.lower()

    country_and_cities.sort()

    valid_country_and_cities = country in country_and_cities
    valid_season = season in seasons

    error_message = ""

    if openai.api_key is None:
        error_message += f"Error occurred in openai API KEY is not found \n "

        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message": error_message, "data": data}
        return templates.TemplateResponse("recommendations.html", context)

    if not valid_country_and_cities:
        error_message += "Error occurred in country or city name, Please select valid Country or City \n"
    if not valid_season:
        error_message += f"Error occurred in season name, Please select season from {seasons}\n "

    if not (valid_country_and_cities and valid_season):
        data['country_and_cities'] = country_and_cities

        context = {'request': request, "error_message": error_message, "data": data}

        return templates.TemplateResponse("recommendations.html", context)

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user",
                       "content": f"What the activity/recommendations in {country} when the season {season} is in it? "
                                  f"write the recommendation without introduction and give 3 recommendation only"}]
        )
        # This line for getting the response text from ChatGPT
        recommendations = response['choices'][0]['message']['content']

        # This for splitting the text into lines to make them in list
        recommendations = recommendations.splitlines()

        # Loop for removing the empty ""
        for space in recommendations:
            if space == "":
                recommendations.remove("")

        data['country'] = country
        data['season'] = season
        data['recommendations'] = recommendations
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "data": data}
        return templates.TemplateResponse("recommendations.html", context)


    except Exception as error_message:
        data['country_and_cities'] = country_and_cities
        context = {'request': request, "error_message": error_message, "data": data}
        return templates.TemplateResponse("recommendations.html", context)
