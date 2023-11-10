from typing import Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}
