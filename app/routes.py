from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import ItemSchema, Request, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items")
async def get_item_service(item: ItemSchema, db: Session = Depends(get_db)):
    _items = crud.get_item(db)
    
    return Response(status="Ok", code="200", message="All items", result=_items).dict(exclude_none=True)

@router.post("/items")
async def create_item_service(item: ItemSchema, db: Session = Depends(get_db)):
    _item = crud.create_item(db=db, item=item)
    
    return Response(status="Ok", code="200", message="Item created", result=_item).dict(exclude_none=True)