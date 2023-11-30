from sqlalchemy.orm import Session
from .models import Item
from .schemas import ItemSchema

def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemSchema):
    db_item = Item(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item