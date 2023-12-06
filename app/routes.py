from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from schemas import ItemSchema, MonsterSchema, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items", status_code=200)
async def get_items_service(db: Session = Depends(get_db)):
    db_item = crud.get_items(db=db)

    return Response(status="Ok", code="200", message="All items", result=db_item).model_dump(exclude_none=True)

@router.get("/items/{item_id}", status_code=200)
async def get_item_by_id_service(item_id: str, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db=db, item_id=item_id)

    return Response(status="Ok", code="200", message=f"Item {item_id}", result=db_item).model_dump(exclude_none=True)

@router.post("/items", status_code=201)
async def create_item_service(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = crud.create_item(db=db, item=item)

    return Response(status="Created", code="201", message="Item created", result=db_item).model_dump(exclude_none=True)

@router.put("/items/{item_id}", status_code=200)
async def update_item(item_id: str, item: ItemSchema, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item=item, item_id=item_id)

    return Response(status="Updated", code="200", message="Item updated", result=db_item).model_dump(exclude_none=True)

@router.get("/monsters", status_code=200)
async def get_monsters_service(db: Session = Depends(get_db)):
    db_monster = crud.get_monster(db=db)

    return Response(status="Ok", code="200", message="All monsters", result=db_monster).model_dump(exclude_none=True)

@router.get("/monsters/{monster_id}", status_code=200)
async def get_monster_by_id_service(monster_id: str, db: Session = Depends(get_db)):
    db_monster = crud.get_monster_by_id(db=db, monster_id=monster_id)

    return Response(status="Ok", code="200", message=f"Monster {monster_id}", result=db_monster).model_dump(exclude_none=True)

@router.post("/monsters", status_code=201)
async def create_monster_service(monster: MonsterSchema, db: Session = Depends(get_db)):
    db_monster = crud.create_monster(db=db, monster=monster)

    return Response(status="Created", code="201", message="Monster created", result=db_monster).model_dump(exclude_none=True)

@router.put("/monsters/{monster_id}", status_code=200)
async def update_monster(monster_id: str, monster: MonsterSchema, db: Session = Depends(get_db)):
    db_monster = crud.update_monster(db=db, monster=monster, monster_id=monster_id)

    return Response(status="Updated", code="200", message="Monster updated", result=db_monster).model_dump(exclude_none=True)
