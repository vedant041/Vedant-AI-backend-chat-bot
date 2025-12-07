from uuid import uuid4
from datetime import datetime
from ..database import complaints_col

def create_complaint(user_id: str, message_text: str) -> dict:
    complaint_id = str(uuid4())
    case_id = f"CMP-{complaint_id[:8].upper()}"
    now = datetime.utcnow()

    doc = {
        "complaint_id": complaint_id,
        "user_id": user_id,
        "case_id": case_id,
        "message_text": message_text,
        "summarized_text": None,
        "intent": None,
        "sentiment_score": None,
        "status": "OPEN",
        "call_result": None,
        "created_at": now,
        "updated_at": now,
    }
    complaints_col.insert_one(doc)
    return doc

def update_analysis(complaint_id: str, analysis: dict) -> dict | None:
    update = {
        "$set": {
            "summarized_text": analysis.get("summary"),
            "intent": analysis.get("intent"),
            "sentiment_score": analysis.get("sentiment_score"),
            "updated_at": datetime.utcnow(),
        }
    }
    complaints_col.update_one({"complaint_id": complaint_id}, update)
    return complaints_col.find_one({"complaint_id": complaint_id})
