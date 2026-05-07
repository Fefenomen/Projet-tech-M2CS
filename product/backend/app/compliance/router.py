"""NIS2 Compliance Dashboard — FastAPI router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.router import get_current_active_user

from .schemas import ComplianceResponse
from .service import compute_nis2_compliance

router = APIRouter(prefix="/compliance", tags=["Compliance"])


@router.get("/nis2", response_model=ComplianceResponse)
def get_nis2_compliance(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """Compute and return NIS2 compliance score and requirements status.

    Requires authentication (admin or analyst).
    """
    try:
        return compute_nis2_compliance(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error computing compliance: {str(e)}",
        )
