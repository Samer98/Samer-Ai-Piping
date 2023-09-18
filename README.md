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

This API for query params
```
http://127.0.0.1:3000//api/recommendations
```
send in query params $country ,  $season
the result will be similar to this
```
{
    "country": "egypt",
    "season": "winter",
    "recommendations": [
        "1. Visit the Pyramids of Giza: Explore one of the Seven Wonders of the Ancient World in a less crowded season. Enjoy the stunning views of the pyramids covered in a picturesque snowfall, and take advantage of the cooler temperatures for a more comfortable visit.",
        "2. Experience a Nile River Cruise: Hop aboard a luxury cruise and meander along the Nile River, taking in the breathtaking landscapes of ancient temples, deserted ruins, and picturesque villages. The cool winter weather provides a pleasant atmosphere to enjoy the scenic beauty of Egypt's iconic waterway.",
        "3. Explore Luxor and Karnak Temples: Discover the fascinating treasures of ancient Egyptian history by visiting the Luxor and Karnak Temples. With mild winter temperatures, you can comfortably explore these vast temple complexes and marvel at their stunning architecture and intricate carvings without battling the intense summer heat."
    ]
}
```

## Documentation 🚀

    FastAPI documentation: https://fastapi.tiangolo.com/
    OpenAI GPT API documentation: https://platform.openai.com/docs/api-referenc
    Docker documentation: https://docs.docker.com/
