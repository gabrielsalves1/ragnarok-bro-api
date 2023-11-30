from pydantic import BaseModel, Field
from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

class ItemSchema(BaseModel):
    id: int
    name: str
    description: str
    weight: float
    price: int
    duration: int
    thrown_on_the_floor: bool
    negotiated: bool
    placed_in_the_warehouse: bool
    stored_in_cart: bool
    sold_to_npc: bool
    placed_in_the_guild_warehouse: bool

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]