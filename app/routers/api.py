from fastapi import APIRouter
from pydantic import BaseModel
from app.database import Base
from app.cache import RedisClient


client = RedisClient()

router = APIRouter()

@router.get("/healthz")
async def healthz():
    return {"Status":"OK"}

@router.get("/redis_healthz")
async def test():
    return client.conn.get('foo')

@router.get("/update")
async def update(uuid: str):
    return uuid

