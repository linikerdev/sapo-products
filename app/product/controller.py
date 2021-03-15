from typing import List

from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/")
def get_products():
    return { "message":"teste"  }
