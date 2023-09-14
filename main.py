from fastapi import FastAPI, HTTPException
import openai
from dotenv import load_dotenv
import os
from country_cities import country_and_cities, seasons


# Function used for getting environment variables
def configure():
    load_dotenv()


configure()

# Api key for openAI
openai.api_key = os.getenv("openai_key")


app = FastAPI()


@app.get("/")
async def home_page():
    return {"message": "Hello to our recommendations website for traveling"}


@app.get("/country_cities")
async def country_cities_list():
    return {"country_and_cities": f"Here are the country_and_cities list {country_and_cities}"}


@app.get("/seasons")
async def season_list():
    return {"season": f"Here are the seasons list {seasons}"}


@app.get("/recommendations")
async def get_recommendations(country: str, season: str):
    season = season.lower()
    country = country.lower()

    error_message = ""
    if openai.api_key is None:
        error_message += f"openai API KEY is not found"
        raise HTTPException(status_code=400, detail={"error_message": error_message})

    if country not in country_and_cities:
        error_message += ("Error occurred in country or city name, Please select Country or City from this link: "
                          "127.0.0.1.3000/country_cities")
        raise HTTPException(status_code=400, detail={"error_message": error_message})

    if season not in seasons:
        error_message += f"Error occurred in season name, Please select season from {seasons} "
        raise HTTPException(status_code=400, detail={"error_message": error_message})

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user",
                       "content": f"What the activity/recommendations in {country} when the season {season} is in it? "
                                  f"write the recommendation without introduction and give 3 recommendation only"}]
        )
        recommendations = response['choices'][0]['message']['content']
        recommendations = recommendations.splitlines()
        for space in recommendations:
            if space == "":
                recommendations.remove("")
        result = {"country": country, "season": season, "recommendations": recommendations}
        return result
    except Exception as error_message:
        raise HTTPException(status_code=400, detail={"error_message": f"{error_message}"})
