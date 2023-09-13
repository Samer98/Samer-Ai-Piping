Ai-Piping Installation and Usage Guide

Welcome to Ai-Piping! This guide will help you install and run the Ai-Piping application using Python and Docker. Ai-Piping is a powerful tool for piping data and leveraging the capabilities of OpenAI. Follow the steps below to get started.
Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

    Python 3.8.10 or a newer version.
    Docker (optional, for Docker installation).

Installation

    Clone the Ai-Piping repository to your local machine:

    bash or cmd

git clone https://github.com/Samer98/Samer-Ai-Piping.git

Navigate to the project directory:

bash or cmd

cd ai-piping

Install the required Python libraries listed in requirements.txt:

bash or cmd

    pip install -r requirements.txt

Running the Application
Using Python

To run the Ai-Piping application using Python, execute the following command:

bash or cmd

uvicorn main:app --reload

This will start the application, and you can access it by opening a web browser and navigating to http://localhost:8000.
Using Docker

If you prefer to run Ai-Piping in a Docker container, follow these steps:

    Build the Docker image with the following command:

    bash or cmd

docker build -t fast-api-app .

Run the Docker container:

bash or cmd

    docker run -d -p 8000:8000 fast-api-app

This will start the Ai-Piping application in a Docker container, and you can access it by opening a web browser and navigating to http://localhost:8000.
Usage

Once the Ai-Piping application is running, you can use it to leverage OpenAI's capabilities for various tasks. Be sure to refer to the API reference and the OpenAI Cookbook for usage examples and guidance on how to make the most of Ai-Piping's features.

feel free to try our api http://127.0.0.1:8000/recommendations?country=$country&season=$season

You will get the best recommendations based on country you're willing to travel to with season.


We welcome contributions from the community. If you have any ideas for improvements or would like to report issues, please create a GitHub issue or submit a pull request.

Thank you for using Ai-Piping! We hope this guide helps you get started quickly and effectively. If you have any questions or need further assistance, feel free to reach out to us.

Happy piping! 🚀