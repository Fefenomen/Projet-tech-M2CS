import time
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user, require_role
from app.core.database import get_db
from app.discovery.schemas import ScanRequest, ScanResponse
from app.discovery import service as discovery_service
from app.models.asset import Asset
from app.models.port import Port
from app.models.audit_log import AuditLog


router = APIRouter()


def _log_action(db: Session, action: str, target_type: str, result: str, user_id: int | None = None, role: str | None = None):
    db.add(AuditLog(
        user_id=user_id,
        role=role,
        action=action,
        target_type=target_type,
        result=result,
    ))
    db.commit()


@router.post("/", response_model=ScanResponse, status_code=status.HTTP_201_CREATED)
async def launch_scan(
    scan_request: ScanRequest,
    db: Session = Depends(get_db),
    admin: dict = Depends(require_role("admin")),
):
    if scan_request.start_ip == scan_request.end_ip:
        ip_range = [scan_request.start_ip]
    else:
        ip_range = discovery_service.ip_range_to_list(scan_request.start_ip, scan_request.end_ip)

    # Security: limit scan range to prevent abuse
    if len(ip_range) > 256:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scan range too large (max 256 IPs)",
        )

    start_time = time.time()
    assets_found = discovery_service.scan_ip_range(
        scan_request.start_ip,
        scan_request.end_ip,
        scan_request.ports,
        scan_request.delay,
    )
    duration = time.time() - start_time

    # Persist discovered assets in DB
    created_count = 0
    for asset_data in assets_found:
        ip = asset_data["ip"]
        existing = db.query(Asset).filter(Asset.ip_address == ip).first()
        if existing:
            existing.last_seen_at = datetime.now(timezone.utc)
            existing.status = "active"
        else:
            asset = Asset(ip_address=ip, hostname=f"host-{ip.replace('.', '-')}", status="active")
            db.add(asset)
            db.flush()
            for port_num in asset_data["ports"]:
                db.add(Port(
                    asset_id=asset.id,
                    port=port_num,
                    protocol="tcp",
                    state="open",
                    service_name=asset_data["services"][asset_data["ports"].index(port_num)] if port_num in asset_data.get("services", []) else None,
                ))
            created_count += 1

    db.commit()

    _log_action(db, "scan_network", "scan_range", "success", role=admin.get("role"))

    return ScanResponse(
        scan_id=f"scan_{int(time.time())}",
        start_ip=scan_request.start_ip,
        end_ip=scan_request.end_ip,
        status="completed",
        assets_found=created_count,
        ports_scanned=len(ip_range) * len(scan_request.ports),
        duration_seconds=round(duration, 2),
    )
