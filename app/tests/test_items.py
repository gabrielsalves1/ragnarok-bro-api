from fastapi import status
from app.tests.test_setup import client

def test_create_item_acaraje(client):
    response = client.post("/items", json={
        "id": "acaraje",
        "name": "Acarajé",
        "description": """Este delicioso quitute brasileiro é feito com inúmeros ingredientes da culinária baiana, \
            desde a massa de feijão-fradinho frita no azeite-de-dendê, até o recheio com camarão, vatapá e caruru. \
            Sem esquecer a pimenta, que deixa a iguaria tão quente e vai deixá-lo elétrico! Precisão +5. Velocidade de ataque +10%. \
            Efeito é cancelado se o usuário morrer. Duração: 20 minutos""",
        "img_url": "img_url",
        "weight": 8,
        "price": 0,
        "thrown_on_the_floor": 0,
        "negotiated": 1,
        "placed_in_the_warehouse": 0,
        "stored_in_cart": 1,
        "sold_to_npc": 0,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['result']['name'] == 'Acarajé'

def test_update_items_acaraje(client):
    client.post("/items", json={
        "id": "acaraje",
        "name": "Acarajé",
        "description": """Este delicioso quitute brasileiro é feito com inúmeros ingredientes da culinária baiana, \
            desde a massa de feijão-fradinho frita no azeite-de-dendê, até o recheio com camarão, vatapá e caruru. \
            Sem esquecer a pimenta, que deixa a iguaria tão quente e vai deixá-lo elétrico! Precisão +5. Velocidade de ataque +10%. \
            Efeito é cancelado se o usuário morrer. Duração: 20 minutos""",
        "img_url": "img_url",
        "weight": 8,
        "price": 0,
        "thrown_on_the_floor": 0,
        "negotiated": 1,
        "placed_in_the_warehouse": 0,
        "stored_in_cart": 1,
        "sold_to_npc": 0,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.put("/items/acaraje", json={
        "id": "acaraje",
        "name": "Acarajé Apimentado",
        "description": """Este delicioso quitute brasileiro é feito com inúmeros ingredientes da culinária baiana, \
            desde a massa de feijão-fradinho frita no azeite-de-dendê, até o recheio com camarão, vatapá e caruru. \
            Sem esquecer a pimenta, que deixa a iguaria tão quente e vai deixá-lo elétrico! Precisão +10. Velocidade de ataque +15%. \
            Efeito é cancelado se o usuário morrer. Duração: 10 minutos""",
        "img_url": "img_url",
        "weight": 16,
        "price": 2,
        "thrown_on_the_floor": 0,
        "negotiated": 1,
        "placed_in_the_warehouse": 0,
        "stored_in_cart": 1,
        "sold_to_npc": 0,
        "placed_in_the_guild_warehouse": 1
    })
    assert response.status_code == status.HTTP_200_OK

def test_get_items_pacote_de_pergaminho(client):
    client.post("/items", json={
        "id": "bundle_of_magic_scroll",
        "name": "Pacote de Pergaminho",
        "description": "Um pergaminho empacotado e embrulhado com cuidado. Produz um Pergaminho Mágico aleatório.",
        "img_url": "img_url",
        "weight": 20,
        "price": 10000,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1
    })

    response = client.get('/items/bundle_of_magic_scroll')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['result'] == {
        "id": "bundle_of_magic_scroll",
        "name": "Pacote de Pergaminho",
        "description": "Um pergaminho empacotado e embrulhado com cuidado. Produz um Pergaminho Mágico aleatório.",
        "img_url": "img_url",
        "weight": 20,
        "price": 10000,
        "thrown_on_the_floor": 1,
        "negotiated": 1,
        "placed_in_the_warehouse": 1,
        "stored_in_cart": 1,
        "sold_to_npc": 1,
        "placed_in_the_guild_warehouse": 1,
        "drop_from_monster_id": None,
        "obtained_from_id": None
    }

def test_not_found_items_pocaomassa(client):
    response = client.get("/items/pocaomassa")
    assert response.status_code == status.HTTP_404_NOT_FOUND
