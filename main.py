from fastapi import FastAPI, HTTPException, Request
import openai
from dotenv import load_dotenv
import os
from country_cities import country_and_cities, seasons

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path




# Function used for getting environment variables
def configure():
    load_dotenv()


# Api key for openAI
openai.api_key = os.getenv("openai_key")

app = FastAPI()

#For getting the static files in the project
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('home.html', context)



@app.get("/country_cities")
async def country_cities_list(request: Request):
    country_and_cities.sort()
    context = {'request': request, "country_and_cities": country_and_cities}
    # return {"country_and_cities": f"Here are the country_and_cities list {country_and_cities}"}
    return templates.TemplateResponse('country_and_cities.html', context)


@app.get("/seasons")
async def season_list(request: Request):
    context = {'request': request, "seasons": seasons}

    return templates.TemplateResponse('season.html', context)


@app.get("/recommendations_page")
async def get_recommendations_page(request: Request):
    context = {'request': request, "result": ""}
    return templates.TemplateResponse("recommendations.html", context)


@app.get("/recommendations")
async def get_recommendations(request: Request, country: str, season: str):
    season = season.lower()
    country = country.lower()

    valid_country_and_cities = country in country_and_cities
    valid_season = season in seasons

    error_message = ""

    if openai.api_key is None:
        error_message += f"Error occurred in openai API KEY is not found \n "
        raise HTTPException(status_code=400, detail={"error_message": error_message})

    if not valid_country_and_cities:
        error_message += "Error occurred in country or city name, Please select Country or City from this link: 127.0.0.1.3000/country_cities\n"
    if not valid_season:
        error_message += f"Error occurred in season name, Please select season from {seasons}\n "

    if not (valid_country_and_cities and valid_season):
        context = {'request': request, "error_message": error_message}

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
        result = {"country": country, "season": season,"recommendations":recommendations}
        context = {'request': request, "result": result}

        return templates.TemplateResponse("recommendations.html",  context)

        # return result

    except Exception as error_message:
        raise HTTPException(status_code=400, detail={"error_message": f"{error_message}"})
