import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

def analyze_text(text: str) -> dict:
    if not client:
        return {
            "summary": text[:100],
            "intent": "general_complaint",
            "sentiment_score": -0.1,
        }

    prompt = f"""You are an assistant for a telecom support team.

Read the complaint below and return a JSON object with keys:
- summary: a short 1–2 line summary
- intent: one of [billing_issue, technical_issue, service_delay, cancellation_request, other]
- sentiment_score: a number between -1 and 1 (negative to positive)

Complaint: {text}
"""

    try:
        resp = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )
        raw = resp.output[0].content[0].text
        return json.loads(raw)
    except Exception as exc:
        print("OpenAI error:", exc)
        return {
            "summary": text[:100],
            "intent": "other",
            "sentiment_score": -0.3,
        }
