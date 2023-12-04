from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Item
from .schemas import ItemSchema

def get_item(db: Session, skip: int = 0, limit: int = 100):
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

    db.query(Item).filter(Item.id == item_id).update({Item.name: item.name, Item.img_url: item.img_url, Item.description: item.description,
                                                    Item.weight: item.weight, Item.description: item.description, Item.price: item.price,
                                                    Item.thrown_on_the_floor: item.thrown_on_the_floor, Item.negotiated: item.negotiated,
                                                    Item.placed_in_the_warehouse: item.placed_in_the_warehouse, Item.stored_in_cart: item.stored_in_cart,
                                                    Item.sold_to_npc: item.sold_to_npc, Item.placed_in_the_guild_warehouse: item.placed_in_the_guild_warehouse})
    db.commit()
    db.refresh(db_item)
    db.close()

    return db_item
