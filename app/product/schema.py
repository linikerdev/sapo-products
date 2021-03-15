from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    """Widget schema"""
    id: Optional[int]
    name: str
    quantidade: int
    proteinas: int
    carboidratos: int
    gorduras: int
