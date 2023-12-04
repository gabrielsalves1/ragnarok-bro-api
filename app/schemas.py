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

class MonsterSchema(BaseModel):
    id: str
    level: int
    race: str
    monster_property: str
    size: str
    base_exp: int
    class_exp: int
    resistence_neutral: int
    resistence_earth: int
    resistence_wind: int
    resistence_holy: int
    resistence_ghost: int
    resistence_water: int
    resistence_fire: int
    resistence_poison: int
    resistence_dark: int
    resistence_curse: int
    hp: int
    attack_min: int
    attack_max: int
    attack_range: int
    precision: int
    dodge: int
    attribute_def: int
    attribute_defm: int
    attribute_for: int
    attribute_agi: int
    attribute_vit: int
    attribute_int: int
    attribute_des: int
    attribute_sor: int

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
