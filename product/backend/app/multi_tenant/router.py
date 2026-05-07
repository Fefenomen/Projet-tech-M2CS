"""Multi-tenant — Router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.core.database import get_db
from app.models.tenant import Tenant

from .schemas import TenantCreate, TenantListResponse, TenantResponse


router = APIRouter(prefix="/tenants", tags=["Multi-tenant"])


@router.get("/", response_model=TenantListResponse)
async def list_tenants(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """List all tenants. Requires admin role."""
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")

    tenants = db.query(Tenant).order_by(Tenant.name).all()
    return TenantListResponse(
        tenants=[
            TenantResponse(
                id=t.id,
                name=t.name,
                description=t.description,
                created_by=t.created_by,
                created_at=t.created_at,
                is_active=t.is_active,
            )
            for t in tenants
        ],
        total=len(tenants),
    )


@router.post("/", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
async def create_tenant(
    tenant_req: TenantCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """Create a new tenant. Requires admin role."""
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")

    existing = db.query(Tenant).filter(Tenant.name == tenant_req.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Tenant already exists")

    tenant = Tenant(
        name=tenant_req.name,
        description=tenant_req.description,
        created_by=current_user["username"],
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    return TenantResponse(
        id=tenant.id,
        name=tenant.name,
        description=tenant.description,
        created_by=tenant.created_by,
        created_at=tenant.created_at,
        is_active=tenant.is_active,
    )
