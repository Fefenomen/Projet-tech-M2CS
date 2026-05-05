from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
import bcrypt

from app.core.config import settings

# Fake user database for MVP (replace with real DB later)
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": bcrypt.hashpw(b"admin123", bcrypt.gensalt()),
        "role": "admin",
        "is_active": True,
    },
    "analyst": {
        "username": "analyst",
        "hashed_password": bcrypt.hashpw(b"analyst123", bcrypt.gensalt()),
        "role": "analyst",
        "is_active": True,
    },
}


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)


def get_user(username: str) -> dict | None:
    return fake_users_db.get(username)


def authenticate_user(username: str, password: str) -> dict | None:
    user = get_user(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str | None = payload.get("sub")
        role: str | None = payload.get("role")
        if username is None:
            return None
        return {"username": username, "role": role}
    except jwt.InvalidTokenError:
        return None
