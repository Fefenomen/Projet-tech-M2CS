from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login():
    return {"message": "Auth endpoint - to be implemented"}


@router.post("/token")
async def token():
    return {"message": "Token endpoint - to be implemented"}
