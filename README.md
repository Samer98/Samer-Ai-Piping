# Ai-Piping Installation and Usage Guide

**Welcome to Ai-Piping!** This guide will assist you in installing and running the Ai-Piping application using both Python and Docker. Ai-Piping is a powerful tool for data processing, utilizing the capabilities of OpenAI. Follow the steps below to get started.

## Prerequisites

Before you begin, ensure that your system meets the following prerequisites:

- Python 3.8.10 or a newer version.
- Docker (optional, for Docker installation).

## Installation

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

## Running the Application

### Using Python

To run the Ai-Piping application using Python, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the application, and you can access it by opening a web browser and navigating to [http://localhost:8000](http://localhost:8000).

### Using Docker

If you prefer to run Ai-Piping in a Docker container, follow these steps:

1. Build the Docker image with the following command:

   ```bash
   docker build -t fast-api-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 fast-api-app
   ```

This will start the Ai-Piping application in a Docker container, and you can access it by opening a web browser and navigating to [http://localhost:8000](http://localhost:8000).

## Usage

Once the Ai-Piping application is running, you can leverage OpenAI's capabilities for various tasks. To get recommendations based on the country you're willing to travel to and the season, you can use the following API endpoint:

```
http://127.0.0.1:8000/recommendations?country=$country&season=$season
```

Be sure to refer to the API reference and the OpenAI Cookbook for usage examples and guidance on how to make the most of Ai-Piping's features.

## Contributing

We welcome contributions from the community. If you have ideas for improvements or would like to report issues, please create a GitHub issue or submit a pull request.

Thank you for choosing Ai-Piping! We hope this guide helps you quickly and effectively get started. If you have any questions or need further assistance, please don't hesitate to reach out to us.

Happy piping! 🚀
