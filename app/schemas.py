from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')

class ItemSchema(BaseModel):
    id: str
    name: str
    img_url: str
    description: str
    weight: float
    price: int
    thrown_on_the_floor: bool
    negotiated: bool
    placed_in_the_warehouse: bool
    stored_in_cart: bool
    sold_to_npc: bool
    placed_in_the_guild_warehouse: bool

    class Config:
        from_attributes = True
        populate_by_name = True

class Request(BaseModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)

class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
