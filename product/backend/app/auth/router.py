from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth.schemas import Token, UserCreate, UserLogin, UserResponse
from app.auth import service as auth_service
from app.core.database import get_db
from app.models.audit_log import AuditLog

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def _log_action(db: Session, action: str, target_type: str, result: str, user_id: int | None = None, role: str | None = None):
    db.add(AuditLog(
        user_id=user_id,
        role=role,
        action=action,
        target_type=target_type,
        result=result,
    ))
    db.commit()


@router.post("/login", response_model=Token)
async def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, user_login.username, user_login.password)
    if not user:
        _log_action(db, "login_failed", "auth", "failed", role="unknown")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=None,
    )
    _log_action(db, "login_success", "auth", "success", user_id=user.id, role=user.role)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token", response_model=Token)
async def login_for_access_token(user_login: UserLogin, db: Session = Depends(get_db)):
    return await login(user_login, db)


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> dict:
    token_data = auth_service.decode_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = auth_service.get_user_by_username(db, token_data["username"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return {"username": user.username, "role": user.role, "is_active": user.is_active}


async def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    if not current_user.get("is_active", False):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def require_role(role: str):
    """Dependency factory to require a specific role."""
    async def role_checker(current_user: dict = Depends(get_current_active_user)) -> dict:
        if current_user.get("role") != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return current_user
    return role_checker


@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: dict = Depends(get_current_active_user)):
    return UserResponse(
        username=current_user["username"],
        role=current_user["role"],
        is_active=current_user["is_active"],
    )


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    db: Session = Depends(get_db),
    admin: dict = Depends(require_role("admin")),
):
    existing = auth_service.get_user_by_username(db, user_create.username)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    new_user = auth_service.create_user(db, user_create.username, user_create.password, user_create.role)
    _log_action(db, "create_user", "user", "success", user_id=new_user.id, role=new_user.role)
    return UserResponse(username=new_user.username, role=new_user.role, is_active=new_user.is_active)
