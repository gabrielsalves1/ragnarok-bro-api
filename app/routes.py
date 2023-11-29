from fastapi import APIRouter
from fastapi import Depends
from .config import SessionLocal
from .schemas import ItemSchema, Request, Response
from sqlalchemy.orm import Session
from . import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items")
async def get_item_service(db: Session = Depends(get_db)):
    _items = crud.get_item(db=db)
    
    return Response(status="Ok", code="200", message="All items", result=_items).dict(exclude_none=True)

@router.get("/items/{item_id}")
async def get_item_service(item_id: int, db: Session = Depends(get_db)):
    _item = crud.get_item_by_id(db=db, item_id=item_id)
    
    return Response(status="Ok", code="200", message=f"Item {item_id}", result=_item).dict(exclude_none=True)

@router.post("/items")
async def create_item_service(item: ItemSchema, db: Session = Depends(get_db)):
    _item = crud.create_item(db=db, item=item)
    
    return Response(status="Ok", code="200", message="Item created", result=_item).dict(exclude_none=True)