from fastapi import FastAPI
import openai

openai_key = "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"
openai.api_key = openai_key

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

seasons  = [ "summer", "winter", "spring", "autumn"]
@app.get("/travel")
async def get_activity(country: str , season: str):
    season = season.lower()
    response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = {"role": "user", "content": f"What the activity/recommendations in {country} when the season {season} is in it?"}
    )
    if season in seasons:
        return {"country": country , "season": season}
    else:
        return {"Error":"Invalid season"}

response = openai.ChatCompletion.create(
model = 'gpt-3.5-turbo',
message = {"role": "user", "content": "What are the activity"}
)
print(response)