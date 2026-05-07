from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models.asset import Asset


def get_all_assets(db: Session) -> list[Asset]:
    return db.query(Asset).order_by(Asset.last_seen_at.desc()).all()


def get_asset_by_id(db: Session, asset_id: int) -> Asset | None:
    return db.query(Asset).filter(Asset.id == asset_id).first()


def update_asset_status(db: Session, asset_id: int, status: str) -> Asset | None:
    asset = get_asset_by_id(db, asset_id)
    if asset:
        asset.status = status
        asset.last_seen_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(asset)
    return asset
