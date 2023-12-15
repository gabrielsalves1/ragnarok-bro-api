from fastapi import status
from app.tests.test_setup import client

def test_create_equipment_placa_buzzy_bol(client):
    response = client.post("/equipments", json={
        "id": "buzzy_ball_board",
        "name": "Placa Buzzy Bol",
        "description": """Uma placa com o símbolo de Buzzy Bol, capaz de tornar o jogador mais ágil e veloz. \
            Aumenta a velocidade de movimento. Tipo: Equipamento para a cabeça Defesa: 0 Equipa em: Topo Peso: 40 \
            Nível necessário: 1 Classes que utilizam: Todas""",
        "img_url": "img_url",
        "weight": 40,
        "price": 50,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['result']['name'] == 'Placa Buzzy Bol'

def test_update_equipment_placa_buzzy_bol(client):
    client.post("/equipments", json={
        "id": "buzzy_ball_board",
        "name": "Placa Buzzy Bol",
        "description": """Uma placa com o símbolo de Buzzy Bol, capaz de tornar o jogador mais ágil e veloz. \
            Aumenta a velocidade de movimento. Tipo: Equipamento para a cabeça Defesa: 0 Equipa em: Topo Peso: 40 \
            Nível necessário: 1 Classes que utilizam: Todas""",
        "img_url": "img_url",
        "weight": 40,
        "price": 50,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.put("/equipments/buzzy_ball_board", json={
        "id": "buzzy_ball_board",
        "name": "Placa Buzzy Bol [Legado]",
        "description": """Uma placa com o símbolo de Buzzy Bol, capaz de tornar o jogador mais ágil e veloz. \
            Aumenta MUITO a velocidade de movimento. Tipo: Equipamento para a cabeça Defesa: 0 Equipa em: Topo Peso: 40 \
            Nível necessário: 1 Classes que utilizam: Todas""",
        "img_url": "img_url",
        "weight": 40,
        "price": 50,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_200_OK

def test_get_equipments_placa_buzzy_bol(client):
    client.post("/equipments", json={
        "id": "buzzy_ball_board",
        "name": "Placa Buzzy Bol",
        "description": """Uma placa com o símbolo de Buzzy Bol, capaz de tornar o jogador mais ágil e veloz. \
            Aumenta a velocidade de movimento. Tipo: Equipamento para a cabeça Defesa: 0 Equipa em: Topo Peso: 40 \
            Nível necessário: 1 Classes que utilizam: Todas""",
        "img_url": "img_url",
        "weight": 40,
        "price": 50,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.get('/equipments/buzzy_ball_board')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['result'] == {
        "id": "buzzy_ball_board",
        "name": "Placa Buzzy Bol",
        "description": """Uma placa com o símbolo de Buzzy Bol, capaz de tornar o jogador mais ágil e veloz. \
            Aumenta a velocidade de movimento. Tipo: Equipamento para a cabeça Defesa: 0 Equipa em: Topo Peso: 40 \
            Nível necessário: 1 Classes que utilizam: Todas""",
        "img_url": "img_url",
        "weight": 40,
        "price": 50,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1,
        "drop_from_monster_id": None,
        "obtained_from_id": None
    }

def test_not_found_equipments_robeemagico(client):
    response = client.get("/equipments/robeemagico")
    assert response.status_code == status.HTTP_404_NOT_FOUND
