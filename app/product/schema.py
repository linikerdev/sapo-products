from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    quantidade: int
    proteinas: int
    carboidratos: int
    gorduras: int
    
    class Config:
        orm_mode = True