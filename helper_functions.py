import os
import openai
from country_cities import country_and_cities, seasons
from dotenv import load_dotenv
# from constants import Singleton
from chatGPT import ChatGPT




def chatGPT_response(country, season):
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

    context = {"country": country, 'season': season, "recommendations": recommendations}
    return context


def is_openAi_key_present():
    # print(ChatGPT.openai.api_key)
    return ChatGPT.openai.api_key is not None


def country_and_season_validation(country, season):
    error_message = []

    if country not in country_and_cities:
        error_message.append(
            "Error occurred in country or city name, Please select valid Country or City ")
    if season not in seasons:
        error_message.append(f"Error occurred in season name, Please select season from {seasons} ")

    return error_message
