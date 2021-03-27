from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/healthz")
async def healthz():
    return {"Status":"OK"}
