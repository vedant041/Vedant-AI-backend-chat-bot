import os
from dotenv import load_dotenv

load_dotenv()

try:
    from twilio.rest import Client
except Exception:
    Client = None

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL")

_twilio = None
if Client and ACCOUNT_SID and AUTH_TOKEN:
    _twilio = Client(ACCOUNT_SID, AUTH_TOKEN)
else:
    print("[Twilio] Missing SID or AUTH TOKEN – real SMS/calls will NOT be sent.")

print("[Twilio] FROM_NUMBER:", FROM_NUMBER)
print("[Twilio] PUBLIC_BASE_URL:", PUBLIC_BASE_URL)


def send_sms(to: str, body: str):
    """Send SMS (or simulate if Twilio not configured)."""
    if not _twilio or not FROM_NUMBER:
        print(f"[Twilio] [SMS simulated] to={to} | {body}")
        return None

    print(f"[Twilio] Sending SMS to {to}")
    return _twilio.messages.create(
        to=to,
        from_=FROM_NUMBER,
        body=body,
    )


def start_outbound_call(to: str, complaint_id: str):
    """
    Start an outbound voice call to `to` using Twilio.
    Twilio will fetch instructions from /voice-outbound-handler.
    """
    if not _twilio or not FROM_NUMBER or not PUBLIC_BASE_URL:
        print(
            f"[Twilio] [CALL simulated] to={to} complaint_id={complaint_id} "
            f"(twilio client or PUBLIC_BASE_URL not configured)"
        )
        return None

    twiml_url = f"{PUBLIC_BASE_URL}/voice-outbound-handler?complaint_id={complaint_id}"
    print(f"[Twilio] Starting REAL outbound call to {to}")
    print(f"[Twilio] TwiML URL: {twiml_url}")

    call = _twilio.calls.create(
        to=to,
        from_=FROM_NUMBER,
        url=twiml_url,
    )

    print("[Twilio] Call started, SID:", call.sid)
    return call
