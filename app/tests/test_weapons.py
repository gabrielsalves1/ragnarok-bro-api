from fastapi import status
from app.tests.test_setup import client

def test_create_weapon_adaga(client):
    response = client.post("/weapons", json={
        "id": "dagger_",
        "name": "Adaga",
        "description": """Faca usada para apunhalar.  Arraste esta arma para sua janela de equipamento para usar.""",
        "img_url": "img_url",
        "weight": 60,
        "price": 14000,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['result']['name'] == 'Adaga'

def test_update_weapon_adaga(client):
    client.post("/weapons", json={
        "id": "dagger_",
        "name": "Adaga",
        "description": """Faca usada para apunhalar.  Arraste esta arma para sua janela de equipamento para usar.""",
        "img_url": "img_url",
        "weight": 60,
        "price": 14000,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.put("/weapons/dagger_", json={
        "id": "dagger_",
        "name": "Adaga +3",
        "description": """Faca usada para apunhalar.  Arraste esta arma para sua janela de equipamento para usar. \
            Tipo: Adaga Força de Ataque: 73 Peso: 60 Nível da arma: 2 Nível necessário: 12""",
        "img_url": "img_url",
        "weight": 60,
        "price": 14000,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_200_OK

def test_get_weapons_adaga_da_boa_ventura(client):
    client.post("/weapons", json={
        "id": "forturn_sword",
        "name": "Adaga da Boa Ventura",
        "description": """Faca encantada que garante muita sorte para seu dono. \
            Esquiva perfeita +20, SOR +5 Tipo: Adaga  Força de Ataque: 90 Peso: 50 Nível da arma: 4 Nível necessário: 25""",
        "img_url": "img_url",
        "weight": 50,
        "price": 20,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.get('/weapons/forturn_sword')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['result'] == {
        "id": "forturn_sword",
        "name": "Adaga da Boa Ventura",
        "description": """Faca encantada que garante muita sorte para seu dono. \
            Esquiva perfeita +20, SOR +5 Tipo: Adaga  Força de Ataque: 90 Peso: 50 Nível da arma: 4 Nível necessário: 25""",
        "img_url": "img_url",
        "weight": 50,
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

def test_not_found_weapons_piike(client):
    response = client.get("/weapons/piike")
    assert response.status_code == status.HTTP_404_NOT_FOUND
