from fastapi import FastAPI
from .routes import health, text_webhook

app = FastAPI(title="Customer Complaint AI - MongoDB")

app.include_router(health.router)
app.include_router(text_webhook.router)

@app.get("/")
def root():
    return {"message": "Service is running"}