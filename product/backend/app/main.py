from fastapi import FastAPI
from app.health.router import router as health_router
from app.core.config import settings

app = FastAPI(
    title="BigBrowser API",
    description="SOC Network Monitoring Platform",
    version="0.1.0",
)

app.include_router(health_router, prefix="/health", tags=["health"])


@app.get("/")
async def root():
    return {
        "service": settings.SERVICE_NAME,
        "version": settings.SERVICE_VERSION,
        "status": "running",
    }
