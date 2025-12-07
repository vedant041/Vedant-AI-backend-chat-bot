from fastapi import APIRouter
from .. import schemas
from ..crud import users, complaints, chat_messages
from ..utils.openai_client import analyze_text
from ..utils.twilio_client import send_sms, start_outbound_call

router = APIRouter()


@router.post("/incoming-text", response_model=schemas.TextComplaintOut)
def incoming_text(payload: schemas.TextComplaintIn):
    user = users.get_or_create_user(payload.phone, payload.full_name)
    complaint = complaints.create_complaint(
        user_id=user["user_id"],
        message_text=payload.message,
    )
    analysis = analyze_text(payload.message)
    complaints.update_analysis(
        complaint_id=complaint["complaint_id"],
        analysis=analysis,
    )
    chat_messages.add_message(
        user_id=user["user_id"],
        complaint_id=complaint["complaint_id"],
        message_type="user",
        text=payload.message,
        ai_summary=analysis.get("summary"),
        intent_tag=analysis.get("intent"),
    )
    confirmation = (
        f"Your complaint has been registered. "
        f"Case ID: {complaint['case_id']}"
    )
    send_sms(payload.phone, confirmation)

    try:
        start_outbound_call(
            to=payload.phone,
            complaint_id=complaint["complaint_id"],
        )
    except Exception as e:
        print("[Twilio] Error starting outbound call:", e)
    return schemas.TextComplaintOut(
        case_id=complaint["case_id"],
        message="Complaint registered successfully.",
    )
