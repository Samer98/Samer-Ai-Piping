Urbano assignment

Ai-Piping

The Ai-Piping installation guide:

The libraries needed to follow up with the Repo will be found in the requirements.txt

You can find usage examples for the OpenAI Python library in our API reference and the OpenAI Cookbook. Installation

To start, ensure you have Python 3.8.10 or newer.

After you have installed the package, to run the app copy the command and run it:

uvicorn main:app --reload

Docker Run:

docker run -d  -p 8000:8000 fast-api-app
