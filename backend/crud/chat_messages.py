from uuid import uuid4
from datetime import datetime
from ..database import chat_messages_col

def add_message(
    user_id: str,
    complaint_id: str,
    message_type: str,
    text: str,
    ai_summary: str | None,
    intent_tag: str | None,
) -> dict:
    doc = {
        "message_id": str(uuid4()),
        "user_id": user_id,
        "complaint_id": complaint_id,
        "message_type": message_type,
        "message_text": text,
        "ai_summary": ai_summary,
        "intent_tag": intent_tag,
        "timestamp": datetime.utcnow(),
    }
    chat_messages_col.insert_one(doc)
    return doc
