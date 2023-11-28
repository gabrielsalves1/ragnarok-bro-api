from sqlalchemy import Boolean, Column, Integer, String, Float
from config import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    weight = Column(Float)
    price = Column(Integer)
    duration = Column(Integer)
    thrown_on_the_floor = Column(Boolean, default=False)
    negotiated = Column(Boolean, default=False)
    placed_in_the_warehouse = Column(Boolean, default=False)
    stored_in_cart = Column(Boolean, default=False)
    sold_to_npc = Column(Boolean, default=False)
    placed_in_the_guild_warehouse = Column(Boolean, default=False)