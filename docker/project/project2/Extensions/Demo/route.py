from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter(prefix="/demo")


@router.get("/")
async def root():
    return {"code": 200, "result": "project2 !"}
