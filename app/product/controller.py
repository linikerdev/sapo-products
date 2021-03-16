from typing import List
from sqlalchemy.sql import func, desc
from app.db import Session, get_db
from .schema import ProductSchema
from .model import Product
from enum import Enum

from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/", response_model=List[ProductSchema])
def get_products(session: Session = Depends(get_db)) -> List[Product]:
    return session.query(Product).order_by(Product.name).all()
 
 
@router.get("/", response_model=List[ProductSchema])
def get_products(session: Session = Depends(get_db)) -> List[Product]:
    return session.query(Product).all()

class FilterType(Enum):
    proteinas = "proteinas"
    carboidratos = "carboidratos"
    gorduras = "gorduras"
    
@router.get("/{filter}")
def get_products(filter:FilterType, session: Session = Depends(get_db)) -> List[Product]:
    def get_filter():
        max_item=session.query(func.max(getattr(Product, filter.value)))
        filter_item=session.query(Product).filter(getattr(Product, filter.value).in_(max_item))
        return filter_item.all()
    
    return get_filter()