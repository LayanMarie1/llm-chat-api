
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

# Create FastAPI application
app = FastAPI(
    title="LLM Chat API",
    description="An API that connects FastAPI with Gemini LLM",
    version="1.0.0"
)


# Define request structure
class ChatRequest(BaseModel):
    message: str


# Define response structure
class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def home():
    return {
        "message": "LLM Chat API is running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=request.message
        )

        return {
            "answer": response.text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
