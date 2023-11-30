from fastapi import APIRouter, Depends
from fastapi import Depends, HTTPException
from .config import SessionLocal
from .schemas import ItemSchema, Response
from sqlalchemy.orm import Session
from . import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items", status_code=200)
async def get_item_service(db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db)

    return Response(status="Ok", code="200", message="All items", result=db_item).dict(exclude_none=True)

@router.get("/items/{item_id}", status_code=200)
async def get_item_service(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Response(status="Ok", code="200", message=f"Item {item_id}", result=db_item).dict(exclude_none=True)

@router.post("/items", status_code=201)
async def create_item_service(item: ItemSchema, db: Session = Depends(get_db)):
    try:
        db_item = crud.create_item(db=db, item=item)
    except:
        raise HTTPException(status_code=409, detail="Conflict, item already exists")

    return Response(status="Created", code="201", message="Item created", result=db_item).dict(exclude_none=True)