
# LLM Chat API

A simple project that connects Google's Gemini LLM with FastAPI.

## Technologies Used

- Python
- FastAPI
- Gemini API
- Docker
- Git and GitHub

## Project Description

This project allows users to send messages through a REST API.
FastAPI receives the message and sends it to the Gemini model.
Gemini generates a response, and the API returns the answer as JSON.

## API Endpoint

POST /chat

Example Request:

{
    "message": "Explain Artificial Intelligence"
}

Example Response:

{
    "answer": "Artificial Intelligence is..."
}

## Run Locally

Install dependencies:

pip install -r requirements.txt

Create a .env file and add:

GEMINI_API_KEY=your_api_key

Run the server:

uvicorn main:app --reload

Open:

http://localhost:8000/docs

## Run with Docker

Build the Docker image:

docker build -t llm-chat-api .

Run the container:

docker run -d --name llm-chat-container -p 8000:8000 --env-file .env llm-chat-api

Open:

http://localhost:8000/docs

## Security

The API key is stored in the .env file and should never be uploaded to GitHub.
