from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.assets.schemas import AssetResponse, AssetDetailResponse, AssetListResponse
from app.assets import service as asset_service
from app.core.database import get_db
from app.risk_scoring.service import compute_asset_risk_score


router = APIRouter()


@router.get("/", response_model=AssetListResponse)
async def list_assets(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    assets = asset_service.get_all_assets(db)
    return AssetListResponse(
        assets=[
            AssetResponse(
                id=a.id,
                ip_address=a.ip_address,
                hostname=a.hostname,
                first_seen_at=a.first_seen_at,
                last_seen_at=a.last_seen_at,
                status=a.status,
            )
            for a in assets
        ],
        total=len(assets),
    )


@router.get("/{asset_id}", response_model=AssetDetailResponse)
async def get_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    asset = asset_service.get_asset_by_id(db, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    ports = [
        {
            "id": p.id,
            "port": p.port,
            "protocol": p.protocol,
            "state": p.state,
            "service_name": getattr(p, "service_name", None),
            "observed_at": p.observed_at,
        }
        for p in asset.ports
    ]

    return AssetDetailResponse(
        id=asset.id,
        ip_address=asset.ip_address,
        hostname=asset.hostname,
        first_seen_at=asset.first_seen_at,
        last_seen_at=asset.last_seen_at,
        status=asset.status,
        ports=ports,
    )


@router.get("/{asset_id}/risk-score")
async def get_asset_risk_score(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    asset = asset_service.get_asset_by_id(db, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    score = compute_asset_risk_score(db, asset)
    return {
        "asset_id": asset.id,
        "ip_address": asset.ip_address,
        "risk_score": score["score"],
        "risk_level": score["level"],
        "factors": score["factors"],
    }
