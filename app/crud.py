from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Item, Monster
from schemas import ItemSchema, MonsterSchema

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item

def create_item(db: Session, item: ItemSchema):
    db_item = Item(**item.model_dump())

    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    except:
        raise HTTPException(status_code=409, detail="Item already exists")

    return db_item

def update_item(item_id: str, db: Session, item: ItemSchema):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.query(Item).filter(Item.id == item_id).update({Item.id: item.id, Item.name: item.name, Item.img_url: item.img_url, Item.description: item.description,
                                                    Item.weight: item.weight, Item.description: item.description, Item.price: item.price,
                                                    Item.thrown_on_the_floor: item.thrown_on_the_floor, Item.negotiated: item.negotiated,
                                                    Item.placed_in_the_warehouse: item.placed_in_the_warehouse, Item.stored_in_cart: item.stored_in_cart,
                                                    Item.sold_to_npc: item.sold_to_npc, Item.placed_in_the_guild_warehouse: item.placed_in_the_guild_warehouse,
                                                    Item.drop_from_monster_id: item.drop_from_monster_id, Item.obtained_from_id: item.obtained_from_id})
    db.commit()
    db.refresh(db_item)
    db.close()

    return db_item

def get_monsters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Monster).offset(skip).limit(limit).all()

def get_monster_by_id(db: Session, monster_id: int):
    db_monster = db.query(Monster).filter(Monster.id == monster_id).first()
    if db_monster is None:
        raise HTTPException(status_code=404, detail="Monster not found")

    return db_monster

def create_monster(db: Session, monster: MonsterSchema):
    db_monster = Monster(**monster.model_dump())

    try:
        db.add(db_monster)
        db.commit()
        db.refresh(db_monster)
    except:
        raise HTTPException(status_code=409, detail="Monster already exists")

    return db_monster

def update_monster(monster_id: str, db: Session, monster: MonsterSchema):
    db_monster = db.query(Monster).filter(Monster.id == monster_id).first()
    if db_monster is None:
        raise HTTPException(status_code=404, detail="Monster not found")

    db.query(Monster).filter(Monster.id == monster_id).update({Monster.id: monster.id, Monster.level: monster.level, Monster.race: monster.race,
                                                            Monster.monster_property: monster.monster_property, Monster.size: monster.size,
                                                            Monster.base_exp: monster.base_exp, Monster.class_exp: monster.class_exp,
                                                            Monster.resistence_neutral: monster.resistence_neutral, Monster.resistence_earth: monster.resistence_earth,
                                                            Monster.resistence_wind: monster.resistence_wind, Monster.resistence_holy: monster.resistence_holy,
                                                            Monster.resistence_ghost: monster.resistence_ghost, Monster.resistence_water: monster.resistence_water,
                                                            Monster.resistence_fire: monster.resistence_fire, Monster.resistence_poison: monster.resistence_poison,
                                                            Monster.resistence_dark: monster.resistence_dark, Monster.resistence_curse: monster.resistence_curse,
                                                            Monster.hp: monster.hp, Monster.attack_min: monster.attack_min,
                                                            Monster.attack_max: monster.attack_max, Monster.attack_range: monster.attack_range,
                                                            Monster.precision: monster.precision, Monster.dodge: monster.dodge,
                                                            Monster.attribute_def: monster.attribute_def, Monster.attribute_defm: monster.attribute_defm,
                                                            Monster.attribute_for: monster.attribute_for, Monster.attribute_agi: monster.attribute_agi,
                                                            Monster.attribute_vit: monster.attribute_vit, Monster.attribute_int: monster.attribute_int,
                                                            Monster.attribute_des: monster.attribute_des, Monster.attribute_sor: monster.attribute_sor})
    db.commit()
    db.refresh(db_monster)
    db.close()

    return db_monster
