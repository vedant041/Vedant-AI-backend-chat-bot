from fastapi import APIRouter
from .health import router as health_router
from .text_webhook import router as text_router
api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(text_router)
__all__ = ["api_router", "health_router", "text_router"]
