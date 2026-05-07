"""NIS2 Compliance Dashboard — schemas Pydantic."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ComplianceItem(BaseModel):
    id: str
    title: str
    description: str
    status: str = "non_conforme"  # conforme, partiellement_conforme, non_conforme
    evidence: Optional[str] = None
    recommendation: str


class Nis2Score(BaseModel):
    overall_score: float = Field(ge=0, le=100)
    total_requirements: int
    compliant_count: int
    partial_count: int
    non_compliant_count: int
    last_updated: datetime


class ComplianceResponse(BaseModel):
    score: Nis2Score
    requirements: list[ComplianceItem]
