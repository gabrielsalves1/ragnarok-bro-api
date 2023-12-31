from sqlalchemy import Boolean, Column, Integer, String, Float, ARRAY
from app.config import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    img_url = Column(String)
    description = Column(String)
    weight = Column(Float)
    price = Column(Integer)
    thrown_on_the_floor = Column(Boolean, default=False)
    negotiated = Column(Boolean, default=False)
    placed_in_the_warehouse = Column(Boolean, default=False)
    stored_in_cart = Column(Boolean, default=False)
    sold_to_npc = Column(Boolean, default=False)
    placed_in_the_guild_warehouse = Column(Boolean, default=False)
    drop_from_monster_id = Column(ARRAY(String))
    obtained_from_id = Column(ARRAY(String))

class Monster(Base):
    __tablename__ = "monsters"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    img_url = Column(String)
    level = Column(Integer)
    race = Column(String)
    monster_property = Column(String)
    size = Column(String)
    base_exp = Column(Integer)
    class_exp = Column(Integer)
    resistence_neutral = Column(Integer)
    resistence_earth = Column(Integer)
    resistence_wind = Column(Integer)
    resistence_holy = Column(Integer)
    resistence_ghost = Column(Integer)
    resistence_water = Column(Integer)
    resistence_fire = Column(Integer)
    resistence_poison = Column(Integer)
    resistence_dark = Column(Integer)
    resistence_curse = Column(Integer)
    hp = Column(Integer)
    attack_min = Column(Integer)
    attack_max = Column(Integer)
    attack_range = Column(Integer)
    precision = Column(Integer)
    dodge = Column(Integer)
    attribute_def = Column(Integer)
    attribute_defm = Column(Integer)
    attribute_for = Column(Integer)
    attribute_agi = Column(Integer)
    attribute_vit = Column(Integer)
    attribute_int = Column(Integer)
    attribute_des = Column(Integer)
    attribute_sor = Column(Integer)
    drop_items_id = Column(ARRAY(String))

class Weapon(Base):
    __tablename__ = "weapons"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    img_url = Column(String)
    description = Column(String)
    weight = Column(Float)
    price = Column(Integer)
    thrown_on_the_floor = Column(Boolean, default=False)
    negotiated = Column(Boolean, default=False)
    placed_in_the_warehouse = Column(Boolean, default=False)
    stored_in_cart = Column(Boolean, default=False)
    sold_to_npc = Column(Boolean, default=False)
    placed_in_the_guild_warehouse = Column(Boolean, default=False)
    drop_from_monster_id = Column(ARRAY(String))
    obtained_from_id = Column(ARRAY(String))

class Equipment(Base):
    __tablename__ = "equipments"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    img_url = Column(String)
    description = Column(String)
    weight = Column(Float)
    price = Column(Integer)
    thrown_on_the_floor = Column(Boolean, default=False)
    negotiated = Column(Boolean, default=False)
    placed_in_the_warehouse = Column(Boolean, default=False)
    stored_in_cart = Column(Boolean, default=False)
    sold_to_npc = Column(Boolean, default=False)
    placed_in_the_guild_warehouse = Column(Boolean, default=False)
    drop_from_monster_id = Column(ARRAY(String))
    obtained_from_id = Column(ARRAY(String))

class Slot(Base):
    __tablename__ = "slots"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    img_url = Column(String)
    description = Column(String)
    weight = Column(Float)
    price = Column(Integer)
    thrown_on_the_floor = Column(Boolean, default=False)
    negotiated = Column(Boolean, default=False)
    placed_in_the_warehouse = Column(Boolean, default=False)
    stored_in_cart = Column(Boolean, default=False)
    sold_to_npc = Column(Boolean, default=False)
    placed_in_the_guild_warehouse = Column(Boolean, default=False)
    drop_from_monster_id = Column(ARRAY(String))
    obtained_from_id = Column(ARRAY(String))
