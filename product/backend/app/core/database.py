from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings


def _engine_kwargs() -> dict:
    if settings.DATABASE_URL.startswith("sqlite"):
        return {"connect_args": {"check_same_thread": False}}
    return {}


engine = create_engine(settings.DATABASE_URL, **_engine_kwargs())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def initialize_database() -> None:
    from app.models import alert, asset, audit_log, export, port, user  # noqa: F401

    Base.metadata.create_all(bind=engine)

    _seed_default_users()


def _seed_default_users() -> None:
    """Create admin and analyst accounts if they don't exist."""
    from app.auth.service import get_password_hash, get_user_by_username
    from app.models.user import User

    with SessionLocal() as db:
        defaults = [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "analyst", "password": "analyst123", "role": "analyst"},
        ]
        for entry in defaults:
            if get_user_by_username(db, entry["username"]) is None:
                db.add(User(
                    username=entry["username"],
                    password_hash=get_password_hash(entry["password"]),
                    role=entry["role"],
                    is_active=True,
                ))
        db.commit()


def check_database_connection() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


def get_db() -> Session:
    """Yield a SQLAlchemy session for request-scoped dependencies."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
