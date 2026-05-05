from fastapi import FastAPI, Depends
from app.health.router import router as health_router
from app.auth.router import router as auth_router, get_current_active_user
from app.telemetry.router import router as telemetry_router
from app.core.config import settings

app = FastAPI(
    title="BigBrowser API",
    description="SOC Network Monitoring Platform",
    version="0.1.0",
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix=f"{settings.API_PREFIX}/auth", tags=["auth"])
app.include_router(telemetry_router, prefix=f"{settings.API_PREFIX}/telemetry", tags=["telemetry"])


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
