from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Item, Monster, Weapon, Equipment, Slot
from schemas import ItemSchema, MonsterSchema, WeaponSchema, EquipmentSchema, SlotSchema

# Items
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

# Monsters
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

    db.query(Monster).filter(Monster.id == monster_id).update({Monster.id: monster.id, Monster.name: monster.name, Monster.img_url: monster.img_url, Monster.level: monster.level, Monster.race: monster.race,
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

# Weapons
def get_weapons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Weapon).offset(skip).limit(limit).all()

def get_weapon_by_id(db: Session, weapon_id: int):
    db_weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")

    return db_weapon

def create_weapon(db: Session, weapon: WeaponSchema):
    db_weapon = Weapon(**weapon.model_dump())

    try:
        db.add(db_weapon)
        db.commit()
        db.refresh(db_weapon)
    except:
        raise HTTPException(status_code=409, detail="Weapon already exists")

    return db_weapon

def update_weapon(weapon_id: str, db: Session, weapon: Weapon):
    db_weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")

    db.query(Weapon).filter(Weapon.id == weapon_id).update({Weapon.id: weapon.id, Weapon.name: weapon.name, Weapon.img_url: weapon.img_url, Weapon.description: weapon.description,
                                                    Weapon.weight: weapon.weight, Weapon.description: weapon.description, Weapon.price: weapon.price,
                                                    Weapon.thrown_on_the_floor: weapon.thrown_on_the_floor, Weapon.negotiated: weapon.negotiated,
                                                    Weapon.placed_in_the_warehouse: weapon.placed_in_the_warehouse, Weapon.stored_in_cart: weapon.stored_in_cart,
                                                    Weapon.sold_to_npc: weapon.sold_to_npc, Weapon.placed_in_the_guild_warehouse: weapon.placed_in_the_guild_warehouse,
                                                    Weapon.drop_from_monster_id: weapon.drop_from_monster_id, Weapon.obtained_from_id: weapon.obtained_from_id})
    db.commit()
    db.refresh(db_weapon)
    db.close()

    return db_weapon

# Equipments
def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Equipment).offset(skip).limit(limit).all()

def get_equipment_by_id(db: Session, equipment_id: int):
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")

    return db_equipment

def create_equipment(db: Session, equipment: EquipmentSchema):
    db_equipment = Equipment(**equipment.model_dump())

    try:
        db.add(db_equipment)
        db.commit()
        db.refresh(db_equipment)
    except:
        raise HTTPException(status_code=409, detail="Equipment already exists")

    return db_equipment

def update_equipment(equipment_id: str, db: Session, equipment: EquipmentSchema):
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")

    db.query(Equipment).filter(Equipment.id == equipment_id).update({Equipment.id: equipment.id, Equipment.name: equipment.name, Equipment.img_url: equipment.img_url, Equipment.description: equipment.description,
                                                    Equipment.weight: equipment.weight, Equipment.description: equipment.description, Equipment.price: equipment.price,
                                                    Equipment.thrown_on_the_floor: equipment.thrown_on_the_floor, Equipment.negotiated: equipment.negotiated,
                                                    Equipment.placed_in_the_warehouse: equipment.placed_in_the_warehouse, Equipment.stored_in_cart: equipment.stored_in_cart,
                                                    Equipment.sold_to_npc: equipment.sold_to_npc, Equipment.placed_in_the_guild_warehouse: equipment.placed_in_the_guild_warehouse,
                                                    Equipment.drop_from_monster_id: equipment.drop_from_monster_id, Equipment.obtained_from_id: equipment.obtained_from_id})
    db.commit()
    db.refresh(db_equipment)
    db.close()

    return db_equipment

# Slots
def get_slots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Slot).offset(skip).limit(limit).all()

def get_slot_by_id(db: Session, slot_id: int):
    db_slot = db.query(Slot).filter(Slot.id == slot_id).first()
    if db_slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")

    return db_slot

def create_slot(db: Session, slot: SlotSchema):
    db_slot = Slot(**slot.model_dump())

    try:
        db.add(db_slot)
        db.commit()
        db.refresh(db_slot)
    except:
        raise HTTPException(status_code=409, detail="Slot already exists")

    return db_slot

def update_slot(slot_id: str, db: Session, slot: SlotSchema):
    db_slot = db.query(Slot).filter(Slot.id == slot_id).first()
    if db_slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")

    db.query(Slot).filter(Slot.id == slot_id).update({Slot.id: slot.id, Slot.name: slot.name, Slot.img_url: slot.img_url, Slot.description: slot.description,
                                                    Slot.weight: slot.weight, Slot.description: slot.description, Slot.price: slot.price,
                                                    Slot.thrown_on_the_floor: slot.thrown_on_the_floor, Slot.negotiated: slot.negotiated,
                                                    Slot.placed_in_the_warehouse: slot.placed_in_the_warehouse, Slot.stored_in_cart: slot.stored_in_cart,
                                                    Slot.sold_to_npc: slot.sold_to_npc, Slot.placed_in_the_guild_warehouse: slot.placed_in_the_guild_warehouse,
                                                    Slot.drop_from_monster_id: slot.drop_from_monster_id, Slot.obtained_from_id: slot.obtained_from_id})
    db.commit()
    db.refresh(db_slot)
    db.close()

    return db_slot