# Ai-Piping Installation and Usage Guide 🚀

**Welcome to Ai-Piping!** This guide will assist you in installing and running the Ai-Piping application using both Python and Docker. Ai-Piping is a powerful tool for data processing, utilizing the capabilities of OpenAI. Follow the steps below to get started.

## Prerequisites 🚀

Before you begin, ensure that your system meets the following prerequisites:

- Python 3.8.10 or a newer version.
- Docker (optional, for Docker installation).

## Installation 🚀

1. Clone the Ai-Piping repository to your local machine:

   ```bash
   git clone https://github.com/Samer98/Samer-Ai-Piping.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ai-piping
   ```

3. Install the required Python libraries listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```
## Configuration 🚀

1. In the project directory create new file .env

2. add variable called openai_key = $openai_key

3. Save the file

## Running the Application 🚀

### Using Python 🚀

To run the Ai-Piping application using Python, execute the following command:

```bash
uvicorn main:app --reload --port 3000
```

This will start the application, and you can access it by opening a web browser and navigating to [http://localhost:3000](http://localhost:3000).

### Using Docker 🚀

If you prefer to run Ai-Piping in a Docker container, follow these steps:

1. Add in the Dockerfile your ENV variables

2. Build the Docker image with the following command:

   ```bash
   docker build -t fast-api-app .
   ```

3. Run the Docker container:

   ```bash
   docker run -d -p 3000:3000 fast-api-app
   ```

This will start the Ai-Piping application in a Docker container, and you can access it by opening a web browser and navigating to [http://localhost:3000](http://localhost:8000).

## Usage 🚀

Once the Ai-Piping application is running, you can leverage OpenAI's capabilities for various tasks. To get recommendations based on the country you're willing to travel to and the season, you can use the following API endpoint:

This API for recommendations page
```
http://127.0.0.1:3000/recommendations_page
```

This API for query params direct
```
http://127.0.0.1:3000/recommendations?country=$country&season=$season
```

Be sure to write valid name for country and season or you might get errors

To check what is the available country/city use this API

```
http://127.0.0.1:3000/country_cities
```

To check what is the available seasons use this API

```
http://127.0.0.1:3000/seasons
```

## Documentation:

    FastAPI documentation: https://fastapi.tiangolo.com/
    OpenAI GPT API documentation: https://platform.openai.com/docs/api-referenc
    Docker documentation: https://docs.docker.com/
