This project is a backend service for handling customer complaints with the help of AI.
Whenever a user sends a message, the system saves it, analyzes it, and assigns a case ID automatically.
Everything is stored in MongoDB, and the API is powered by FastAPI.

Tech stack used:
FastAPI - Web framework
MongoDB - Database
OpenAI API - To generate summaries, detect intent, and score sentiment
Twilio - For sending SMS confirmations
Collections used in the database:
users, complaints, chat_messages, call_sessions, ai_memory.

1. Setup (Windows)
Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate
Install the project dependencies:
pip install -r requirements.txt

2. Running the Server

Start the API using:
uvicorn backend.main:app --reload

Useful URLs:
API Home - http://127.0.0.1:8000/
API Docs - http://127.0.0.1:8000/docs

Available endpoints include:
GET / - Basic check
GET /health - Server health
POST /incoming-text - Main complaint intake route

3. Testing Complaint Submission
Go to the Swagger docs (/docs):
Find POST /incoming-text
