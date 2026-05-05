from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": settings.SERVICE_NAME,
        "version": settings.SERVICE_VERSION,
    }
