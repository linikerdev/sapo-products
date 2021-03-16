from sqlalchemy import Integer, Column, String
from app.db import Base

from .schema import ProductSchema

class Product(Base):  # type: ignore

    __tablename__ = "product"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    quantidade = Column(Integer())
    proteinas = Column(Integer())
    carboidratos = Column(Integer())
    gorduras = Column(Integer())
    
    def update(self, changes: ProductSchema):
        for key, val in changes.dict().items():
            setattr(self, key, val)
        return self
