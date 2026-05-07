from fastapi import APIRouter

from app.core.config import settings
from app.core.database import check_database_connection

router = APIRouter()


@router.get("/")
async def health_check():
    database_ok = check_database_connection()
    return {
        "status": "ok" if database_ok else "degraded",
        "service": settings.SERVICE_NAME,
        "version": settings.SERVICE_VERSION,
        "database": "ok" if database_ok else "error",
    }
