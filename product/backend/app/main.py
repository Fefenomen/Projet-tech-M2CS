from contextlib import asynccontextmanager
import os

from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.health.router import router as health_router
from app.auth.router import router as auth_router, get_current_active_user
from app.telemetry.router import router as telemetry_router
from app.discovery.router import router as discovery_router
from app.assets.router import router as assets_router
from app.alerts.router import router as alerts_router
from app.reports.router import router as reports_router
from app.audit.router import router as audit_router
from app.dashboard.router import router as dashboard_router
from app.traffic.router import router as traffic_router
from app.compliance.router import router as compliance_router
from app.api_v2.router import router as api_v2_router
from app.multi_tenant.router import router as multi_tenant_router
from app.i18n.router import router as i18n_router
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
app.include_router(dashboard_router, prefix=f"{settings.API_PREFIX}/dashboard", tags=["dashboard"])
app.include_router(reports_router, prefix=f"{settings.API_PREFIX}/exports", tags=["reports"])
app.include_router(audit_router, prefix=f"{settings.API_PREFIX}/audit-logs", tags=["audit"])
app.include_router(traffic_router, prefix=f"{settings.API_PREFIX}/traffic", tags=["traffic"])
app.include_router(compliance_router, prefix=f"{settings.API_PREFIX}", tags=["compliance"])
app.include_router(api_v2_router, prefix="/api/v2", tags=["API v2"])
app.include_router(multi_tenant_router, prefix=settings.API_PREFIX, tags=["multi-tenant"])
app.include_router(i18n_router, prefix="/api", tags=["i18n"])

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "frontend")

if os.path.isdir(os.path.join(FRONTEND_DIR, "static")):
    app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR, "static")), name="static")


@app.get("/")
async def root():
    index_path = os.path.join(FRONTEND_DIR, "templates", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "service": settings.SERVICE_NAME,
        "version": settings.SERVICE_VERSION,
        "status": "running",
    }


@app.get("/api/v1/protected")
async def protected_route(user: dict = Depends(get_current_active_user)):
    return {"message": "Access granted", "user": user["username"], "role": user["role"]}
