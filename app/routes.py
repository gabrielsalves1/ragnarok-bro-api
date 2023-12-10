from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from schemas import ItemSchema, MonsterSchema, WeaponSchema, EquipmentSchema, SlotSchema, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Items
@router.get("/items", status_code=200)
async def get_items_service(db: Session = Depends(get_db)):
    db_items = crud.get_items(db=db)

    return Response(status="Ok", code="200", message="All items", result=db_items).model_dump(exclude_none=True)

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

# Monsters
@router.get("/monsters", status_code=200)
async def get_monsters_service(db: Session = Depends(get_db)):
    db_monsters = crud.get_monsters(db=db)

    return Response(status="Ok", code="200", message="All monsters", result=db_monsters).model_dump(exclude_none=True)

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

# Weapons
@router.get("/weapons", status_code=200)
async def get_weapons_service(db: Session = Depends(get_db)):
    db_weapons = crud.get_weapons(db=db)

    return Response(status="Ok", code="200", message="All weapons", result=db_weapons).model_dump(exclude_none=True)

@router.get("/weapons/{weapon_id}", status_code=200)
async def get_weapon_by_id_service(weapon_id: str, db: Session = Depends(get_db)):
    db_weapon = crud.get_weapon_by_id(db=db, weapon_id=weapon_id)

    return Response(status="Ok", code="200", message=f"Weapon {weapon_id}", result=db_weapon).model_dump(exclude_none=True)

@router.post("/weapons", status_code=201)
async def create_weapon_service(weapon: WeaponSchema, db: Session = Depends(get_db)):
    db_weapon = crud.create_weapon(db=db, weapon=weapon)

    return Response(status="Created", code="201", message="Weapon created", result=db_weapon).model_dump(exclude_none=True)

@router.put("/weapons/{weapon_id}", status_code=200)
async def update_weapon(weapon_id: str, weapon: WeaponSchema, db: Session = Depends(get_db)):
    db_weapon = crud.update_weapon(db=db, weapon=weapon, weapon_id=weapon_id)

    return Response(status="Updated", code="200", message="Weapon updated", result=db_weapon).model_dump(exclude_none=True)

# Equipments
@router.get("/equipments", status_code=200)
async def get_equipments_service(db: Session = Depends(get_db)):
    db_equipments = crud.get_equipments(db=db)

    return Response(status="Ok", code="200", message="All equipments", result=db_equipments).model_dump(exclude_none=True)

@router.get("/equipments/{equipment_id}", status_code=200)
async def get_equipment_by_id_service(equipment_id: str, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment_by_id(db=db, equipment_id=equipment_id)

    return Response(status="Ok", code="200", message=f"Equipment {equipment_id}", result=db_equipment).model_dump(exclude_none=True)

@router.post("/equipments", status_code=201)
async def create_equipment_service(equipment: EquipmentSchema, db: Session = Depends(get_db)):
    db_equipment = crud.create_equipment(db=db, equipment=equipment)

    return Response(status="Created", code="201", message="Equipment created", result=db_equipment).model_dump(exclude_none=True)

@router.put("/equipments/{equipment_id}", status_code=200)
async def update_equipment(equipment_id: str, equipment: EquipmentSchema, db: Session = Depends(get_db)):
    db_equipment = crud.update_equipment(db=db, equipment=equipment, equipment_id=equipment_id)

    return Response(status="Updated", code="200", message="Equipment updated", result=db_equipment).model_dump(exclude_none=True)

# Slots
@router.get("/slots", status_code=200)
async def get_slots_service(db: Session = Depends(get_db)):
    db_slots = crud.get_slots(db=db)

    return Response(status="Ok", code="200", message="All slots", result=db_slots).model_dump(exclude_none=True)

@router.get("/slots/{slot_id}", status_code=200)
async def get_slot_by_id_service(slot_id: str, db: Session = Depends(get_db)):
    db_slot = crud.get_slot_by_id(db=db, slot_id=slot_id)

    return Response(status="Ok", code="200", message=f"Slot {slot_id}", result=db_slot).model_dump(exclude_none=True)

@router.post("/slots", status_code=201)
async def create_slot_service(slot: SlotSchema, db: Session = Depends(get_db)):
    db_slot = crud.create_slot(db=db, slot=slot)

    return Response(status="Created", code="201", message="Slot created", result=db_slot).model_dump(exclude_none=True)

@router.put("/slots/{slot_id}", status_code=200)
async def update_slot(slot_id: str, slot: SlotSchema, db: Session = Depends(get_db)):
    db_slot = crud.update_slot(db=db, slot=slot, slot_id=slot_id)

    return Response(status="Updated", code="200", message="Slot updated", result=db_slot).model_dump(exclude_none=True)
