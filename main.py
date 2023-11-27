from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql_app.models import Item
from sql_app.database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Welcome to Ragnarok API! It's a web scraping from bRO official database, go to /docs to see docs and endpoints."}

@app.post('/items')
async def create_item(id: int, name: str, description: str, weight: float, price: int, duration: int, thrown_on_the_floor: bool,
                        negotiated: bool, placed_in_the_warehouse: bool, stored_in_cart: bool, sold_to_npc: bool,
                        placed_in_the_guild_warehouse: bool, db: Session = Depends(get_db)):    
    item = Item(id=id, name=name, description=description, weight=weight, price=price, duration=duration, thrown_on_the_floor=False,
                        negotiated=False, placed_in_the_warehouse=False, stored_in_cart=False, sold_to_npc=False,
                        placed_in_the_guild_warehouse=False)

    db.add(item)
    db.commit()
    
    return item