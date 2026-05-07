from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user, require_role
from app.audit.schemas import AuditLogItemResponse, AuditLogListResponse
from app.audit import service as audit_service
from app.core.database import get_db


router = APIRouter()


@router.get("/", response_model=AuditLogListResponse)
async def list_audit_logs(
    db: Session = Depends(get_db),
    admin: dict = Depends(require_role("admin")),
):
    logs = audit_service.get_all_audit_logs(db)
    return AuditLogListResponse(
        logs=[
            AuditLogItemResponse(
                id=log.id,
                user_id=log.user_id,
                role=log.role,
                action=log.action,
                target_type=log.target_type,
                result=log.result,
                created_at=log.created_at,
            )
            for log in logs
        ],
        total=len(logs),
    )


@router.get("/{log_id}", response_model=AuditLogItemResponse)
async def get_audit_log(
    log_id: int,
    db: Session = Depends(get_db),
    admin: dict = Depends(require_role("admin")),
):
    log = audit_service.get_audit_log_by_id(db, log_id)
    if not log:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Audit log not found")

    return AuditLogItemResponse(
        id=log.id,
        user_id=log.user_id,
        role=log.role,
        action=log.action,
        target_type=log.target_type,
        result=log.result,
        created_at=log.created_at,
    )
