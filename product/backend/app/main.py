from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.health.router import router as health_router
from app.auth.router import router as auth_router, get_current_active_user
from app.telemetry.router import router as telemetry_router
from app.discovery.router import router as discovery_router
from app.assets.router import router as assets_router
from app.alerts.router import router as alerts_router
from app.core.config import settings
from app.core.database import initialize_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_database()
    yield

app = FastAPI(
    title="BigBrowser API",
    description="SOC Network Monitoring Platform",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix=f"{settings.API_PREFIX}/auth", tags=["auth"])
app.include_router(telemetry_router, prefix=f"{settings.API_PREFIX}/telemetry", tags=["telemetry"])
app.include_router(discovery_router, prefix=f"{settings.API_PREFIX}/scan", tags=["discovery"])
app.include_router(assets_router, prefix=f"{settings.API_PREFIX}/assets", tags=["assets"])
app.include_router(alerts_router, prefix=f"{settings.API_PREFIX}/alerts", tags=["alerts"])


@app.get("/")
async def root():
    return {
        "service": settings.SERVICE_NAME,
        "version": settings.SERVICE_VERSION,
        "status": "running",
    }


@app.get("/api/v1/protected")
async def protected_route(user: dict = Depends(get_current_active_user)):
    return {"message": "Access granted", "user": user["username"], "role": user["role"]}
