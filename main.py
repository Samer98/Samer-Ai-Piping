from fastapi import FastAPI, HTTPException
import openai
from dotenv import load_dotenv
import os
from country_cities import country_and_cities, seasons




def configure():
    load_dotenv()


configure()

openai.api_key = os.getenv("openai_key")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recommendations")
async def get_activity(country: str, season: str):
    season = season.lower()
    country = country.lower()

    if season not in seasons:
        raise HTTPException(status_code=400, detail="Wrong season, please check the season")
    if country not in country_and_cities:
        raise HTTPException(status_code=400, detail="Wrong Country or city, please re-check again")

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user",
                   "content": f"What the activity/recommendations in {country} when the season {season} is in it? write the recommendation without introduction"}]
    )
    recommendations = response['choices'][0]['message']['content']
    recommendations = recommendations.splitlines()
    for space in recommendations:
        if space == "":
            recommendations.remove("")
    result = {"country": country, "season": season, "recommendations": recommendations}
    return result
