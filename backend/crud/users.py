from uuid import uuid4
from ..database import users_col

def get_user_by_phone(phone: str) -> dict | None:
    return users_col.find_one({"phone_number": phone})

def create_user(phone: str, full_name: str | None) -> dict:
    user_id = str(uuid4())
    doc = {
        "user_id": user_id,
        "full_name": full_name,
        "phone_number": phone,
        "preferred_language": None,
    }
    users_col.insert_one(doc)
    return doc

def get_or_create_user(phone: str, full_name: str | None) -> dict:
    existing = get_user_by_phone(phone)
    if existing:
        return existing
    return create_user(phone, full_name)
