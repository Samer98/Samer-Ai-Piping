from fastapi import FastAPI
import openai

openai_key = "sk-p5yuUPAueZtestOpwT3BlbkFJom0jS"
openai.api_key = openai_key

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

seasons  = [ "summer", "winter", "spring", "autumn"]
@app.get("/recommendations")
async def get_activity(country: str , season: str):
    season = season.lower()

    if season not in seasons:
        return {"Error":"Invalid season"}

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role": "user", "content": f"What the activity/recommendations in {country} when the season {season} is in it? write the recommendation without introduction"}]
        )
    recommendations = response['choices'][0]['message']['content']
    recommendations = recommendations.splitlines()
    for space in recommendations:
        if space == "":
            recommendations.remove("")
    result = {"country":country,"season":season,"recommendations":recommendations}
    return result


