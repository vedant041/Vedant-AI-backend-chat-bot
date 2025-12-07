from pydantic import BaseModel
from typing import Optional

class TextComplaintIn(BaseModel):
    phone: str
    message: str
    full_name: Optional[str] = None

class TextComplaintOut(BaseModel):
    case_id: str
    message: str
