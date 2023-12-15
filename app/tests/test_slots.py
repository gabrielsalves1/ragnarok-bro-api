from fastapi import status
from app.tests.test_setup import client

def test_create_slot_fabre_card(client):
    response = client.post("/slots", json={
        "id": "fabre_card",
        "name": "Carta Fabre",
        "description": """Máx. HP +100, VIT +1 \
            Combine com um item para utilizar sua propriedade. \
            Classe: Carta \
            Combina com: Armamento""",
        "img_url": "img_url",
        "weight": 1,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['result']['name'] == 'Carta Fabre'

def test_update_slot_fabre_card(client):
    client.post("/slots", json={
        "id": "fabre_card",
        "name": "Carta Fabre",
        "description": """Máx. HP +100, VIT +1 \
            Combine com um item para utilizar sua propriedade. \
            Classe: Carta \
            Combina com: Armamento""",
        "img_url": "img_url",
        "weight": 1,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.put("/slots/fabre_card", json={
        "id": "fabre_card",
        "name": "Carta Fabre",
        "description": """Máx. HP +300, VIT -1, INT +3 \
            Combine com um item para utilizar sua propriedade. \
            Classe: Carta \
            Combina com: Armamento""",
        "img_url": "img_url",
        "weight": 1,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_200_OK

def test_get_slots_fabre_card(client):
    client.post("/slots", json={
        "id": "fabre_card",
        "name": "Carta Fabre",
        "description": """Máx. HP +100, VIT +1 \
            Combine com um item para utilizar sua propriedade. \
            Classe: Carta \
            Combina com: Armamento""",
        "img_url": "img_url",
        "weight": 1,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.get('/slots/fabre_card')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['result'] == {
        "id": "fabre_card",
        "name": "Carta Fabre",
        "description": """Máx. HP +100, VIT +1 \
            Combine com um item para utilizar sua propriedade. \
            Classe: Carta \
            Combina com: Armamento""",
        "img_url": "img_url",
        "weight": 1,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1,
        "drop_from_monster_id": None,
        "obtained_from_id": None
    }

def test_not_found_slots_cardthan(client):
    response = client.get("/slots/cardthan")
    assert response.status_code == status.HTTP_404_NOT_FOUND
