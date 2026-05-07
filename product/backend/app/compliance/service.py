"""NIS2 Compliance Dashboard — business logic."""

from datetime import datetime, timezone
from typing import Callable

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord
from app.models.user import User
from app.telemetry.service import events_store

from .schemas import ComplianceItem, ComplianceResponse, Nis2Score


def _check_network_supervision(db: Session) -> tuple[str, str, str]:
    asset_count = db.query(func.count(Asset.id)).scalar() or 0
    event_count = len(events_store)
    if asset_count >= 2 and event_count >= 5:
        return "conforme", f"{asset_count} assets, {event_count} events", ""
    elif asset_count >= 1 or event_count >= 1:
        return "partiellement_conforme", f"{asset_count} assets, {event_count} events", "Ajouter des endpoints supervisés"
    return "non_conforme", "Aucun asset détecté", "Configurer un scan réseau ou connecter un agent"


def _check_alert_management(db: Session) -> tuple[str, str, str]:
    alert_count = db.query(func.count(Alert.id)).scalar() or 0
    closed_count = db.query(func.count(Alert.id)).filter(Alert.status == "closed").scalar() or 0
    if alert_count >= 1 and closed_count >= 1:
        return "conforme", f"{alert_count} alertes ({closed_count} clôturées)", ""
    elif alert_count >= 1:
        return "partiellement_conforme", f"{alert_count} alertes (aucune clôturée)", "Qualifier et clôturer des alertes"
    return "non_conforme", "Aucune alerte", "Générer des événements suspects"


def _check_access_logging(db: Session) -> tuple[str, str, str]:
    log_count = db.query(func.count(AuditLog.id)).scalar() or 0
    if log_count >= 5:
        return "conforme", f"{log_count} entrées d'audit", ""
    elif log_count >= 1:
        return "partiellement_conforme", f"{log_count} entrées d'audit", "Augmenter la journalisation"
    return "non_conforme", "Aucun journal d'audit", "Vérifier que les actions sont tracées"


def _check_asset_inventory(db: Session) -> tuple[str, str, str]:
    asset_count = db.query(func.count(Asset.id)).scalar() or 0
    if asset_count >= 3:
        return "conforme", f"{asset_count} actifs inventoriés", ""
    elif asset_count >= 1:
        return "partiellement_conforme", f"{asset_count} actif(s)", "Scanner la plage réseau complète"
    return "non_conforme", "Aucun actif", "Lancer un scan réseau"


def _check_proof_export(db: Session) -> tuple[str, str, str]:
    export_count = db.query(func.count(ExportRecord.id)).scalar() or 0
    if export_count >= 1:
        return "conforme", f"{export_count} export(s) généré(s)", ""
    return "non_conforme", "Aucun export", "Générer un export CSV ou JSON"


def _check_access_control(db: Session) -> tuple[str, str, str]:
    user_count = db.query(func.count(User.id)).scalar() or 0
    role_count = db.query(func.count(User.id)).filter(User.role == "admin").scalar() or 0
    if user_count >= 2 and role_count >= 1:
        return "conforme", f"{user_count} utilisateurs, {role_count} admin(s)", ""
    elif user_count >= 1:
        return "partiellement_conforme", f"{user_count} utilisateur(s)", "Créer un compte analyste"
    return "non_conforme", "Aucun utilisateur", "Initialiser les comptes"


def _check_incident_detection(db: Session) -> tuple[str, str, str]:
    alert_count = db.query(func.count(Alert.id)).scalar() or 0
    if alert_count >= 1:
        return "conforme", f"{alert_count} alerte(s) détectée(s)", ""
    return "non_conforme", "Aucune alerte détectée", "Configurer les règles de détection"


def _check_telemetry_collection(db: Session) -> tuple[str, str, str]:
    event_count = len(events_store)
    if event_count >= 10:
        return "conforme", f"{event_count} événements collectés", ""
    elif event_count >= 1:
        return "partiellement_conforme", f"{event_count} événement(s)", "Connecter plus d'endpoints"
    return "non_conforme", "Aucun événement", "Configurer l'agent endpoint"


# 8 exigences NIS2 pour le MVP
NIS2_REQUIREMENTS: list[dict] = [
    {
        "id": "NIS2-01",
        "title": "Supervision réseau",
        "description": "L'organisation dispose d'une supervision continue de son réseau.",
        "check": _check_network_supervision,
    },
    {
        "id": "NIS2-02",
        "title": "Gestion des alertes",
        "description": "Un système d'alertes permet de qualifier et traiter les incidents.",
        "check": _check_alert_management,
    },
    {
        "id": "NIS2-03",
        "title": "Journalisation des accès",
        "description": "Les connexions et actions sensibles sont journalisées.",
        "check": _check_access_logging,
    },
    {
        "id": "NIS2-04",
        "title": "Inventaire des actifs",
        "description": "Un inventaire des équipements réseau est maintenu à jour.",
        "check": _check_asset_inventory,
    },
    {
        "id": "NIS2-05",
        "title": "Export de preuves",
        "description": "Des exports CSV/JSON permettent de prouver la conformité.",
        "check": _check_proof_export,
    },
    {
        "id": "NIS2-06",
        "title": "Contrôle d'accès",
        "description": "L'accès à l'outil est protégé par authentification et rôles.",
        "check": _check_access_control,
    },
    {
        "id": "NIS2-07",
        "title": "Détection d'incidents",
        "description": "Des règles de détection identifient les comportements suspects.",
        "check": _check_incident_detection,
    },
    {
        "id": "NIS2-08",
        "title": "Collecte de télémétrie",
        "description": "Les endpoints supervisés remontent des événements régulièrement.",
        "check": _check_telemetry_collection,
    },
]


def compute_nis2_compliance(db: Session) -> ComplianceResponse:
    requirements = []
    compliant = 0
    partial = 0
    non_compliant = 0

    for req in NIS2_REQUIREMENTS:
        status, evidence, recommendation = req["check"](db)
        if status == "conforme":
            compliant += 1
        elif status == "partiellement_conforme":
            partial += 1
        else:
            non_compliant += 1

        requirements.append(
            ComplianceItem(
                id=req["id"],
                title=req["title"],
                description=req["description"],
                status=status,
                evidence=evidence,
                recommendation=recommendation,
            )
        )

    total = len(NIS2_REQUIREMENTS)
    score_value = (compliant * 100 + partial * 50) / total

    return ComplianceResponse(
        score=Nis2Score(
            overall_score=round(score_value, 1),
            total_requirements=total,
            compliant_count=compliant,
            partial_count=partial,
            non_compliant_count=non_compliant,
            last_updated=datetime.now(timezone.utc),
        ),
        requirements=requirements,
    )
