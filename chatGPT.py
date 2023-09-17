import openai
import os
from dotenv import load_dotenv
from abc import ABC

def configure():
    load_dotenv()


configure()

class ChatGPT():
    _openai = openai
    _openai.api_key = os.getenv("openai_key")

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")


    @staticmethod
    def get_travel_recommendations(country, season):
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

        # context = {"country": country, 'season': season, "recommendations": recommendations}
        return recommendations

    @staticmethod
    def is_key_present(self):
        return self.openai.api_key is not None


