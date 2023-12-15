from fastapi import status
from app.tests.test_setup import client

def test_create_monster_poring(client):
    response = client.post("/monsters", json={
        "id": "poring",
        "name": "Poring",
        "level": 1,
        "race": "Planta",
        "img_url": "img_url",
        "monster_property": "Água 1",
        "size": "Médio",
        "base_exp": 1,
        "class_exp": 1,
        "resistence_neutral": 100,
        "resistence_earth": 100,
        "resistence_wind": 175,
        "resistence_holy": 100,
        "resistence_ghost": 100,
        "resistence_water": 25,
        "resistence_fire": 90,
        "resistence_poison": 100,
        "resistence_dark": 100,
        "resistence_curse": 100,
        "hp": 50,
        "attack_min": 7,
        "attack_max": 10,
        "attack_range": 1,
        "precision": 202,
        "dodge": 207,
        "attribute_def": 0,
        "attribute_defm": 5,
        "attribute_for": 1,
        "attribute_agi": 1,
        "attribute_vit": 1,
        "attribute_int": 0,
        "attribute_des": 6,
        "attribute_sor": 30
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['result']['name'] == 'Poring'

def test_update_monster_salgueiro_anciao(client):
    client.post("/monsters", json={
        "id": "elder_wilow",
        "name": "Salgueiro Ancião",
        "level": 34,
        "race": "Planta",
        "img_url": "img_url",
        "monster_property": "Fogo 2",
        "size": "Médio",
        "base_exp": 233,
        "class_exp": 263,
        "resistence_neutral": 100,
        "resistence_earth": 90,
        "resistence_wind": 100,
        "resistence_holy": 100,
        "resistence_ghost": 75,
        "resistence_water": 175,
        "resistence_fire": 0,
        "resistence_poison": 125,
        "resistence_dark": 100,
        "resistence_curse": 75,
        "hp": 599,
        "attack_min": 80,
        "attack_max": 94,
        "attack_range": 1,
        "precision": 248,
        "dodge": 263,
        "attribute_def": 45,
        "attribute_defm": 0,
        "attribute_for": 10,
        "attribute_agi": 14,
        "attribute_vit": 25,
        "attribute_int": 0,
        "attribute_des": 29,
        "attribute_sor": 0
    })

    response = client.put("/monsters/elder_wilow", json={
        "id": "elder_wilow",
        "name": "Salgueiro Ancião",
        "level": 34,
        "race": "Planta",
        "img_url": "img_url",
        "monster_property": "Fogo 3",
        "size": "Médio",
        "base_exp": 333,
        "class_exp": 463,
        "resistence_neutral": 100,
        "resistence_earth": 90,
        "resistence_wind": 100,
        "resistence_holy": 100,
        "resistence_ghost": 75,
        "resistence_water": 200,
        "resistence_fire": 0,
        "resistence_poison": 125,
        "resistence_dark": 100,
        "resistence_curse": 75,
        "hp": 700,
        "attack_min": 80,
        "attack_max": 94,
        "attack_range": 1,
        "precision": 248,
        "dodge": 263,
        "attribute_def": 45,
        "attribute_defm": 0,
        "attribute_for": 10,
        "attribute_agi": 14,
        "attribute_vit": 25,
        "attribute_int": 0,
        "attribute_des": 29,
        "attribute_sor": 0
    })
    assert response.status_code == status.HTTP_200_OK

def test_get_monster_poring(client):
    client.post("/monsters", json={
        "id": "poring",
        "name": "Poring",
        "level": 1,
        "race": "Planta",
        "img_url": "img_url",
        "monster_property": "Água 1",
        "size": "Médio",
        "base_exp": 1,
        "class_exp": 1,
        "resistence_neutral": 100,
        "resistence_earth": 100,
        "resistence_wind": 175,
        "resistence_holy": 100,
        "resistence_ghost": 100,
        "resistence_water": 25,
        "resistence_fire": 90,
        "resistence_poison": 100,
        "resistence_dark": 100,
        "resistence_curse": 100,
        "hp": 50,
        "attack_min": 7,
        "attack_max": 10,
        "attack_range": 1,
        "precision": 202,
        "dodge": 207,
        "attribute_def": 0,
        "attribute_defm": 5,
        "attribute_for": 1,
        "attribute_agi": 1,
        "attribute_vit": 1,
        "attribute_int": 0,
        "attribute_des": 6,
        "attribute_sor": 30,
        "drop_items_id": ["jellopy", "Poring Card"]
    })

    response = client.get('/monsters/poring')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['result'] == {
        "id": "poring",
        "name": "Poring",
        "level": 1,
        "race": "Planta",
        "img_url": "img_url",
        "monster_property": "Água 1",
        "size": "Médio",
        "base_exp": 1,
        "class_exp": 1,
        "resistence_neutral": 100,
        "resistence_earth": 100,
        "resistence_wind": 175,
        "resistence_holy": 100,
        "resistence_ghost": 100,
        "resistence_water": 25,
        "resistence_fire": 90,
        "resistence_poison": 100,
        "resistence_dark": 100,
        "resistence_curse": 100,
        "hp": 50,
        "attack_min": 7,
        "attack_max": 10,
        "attack_range": 1,
        "precision": 202,
        "dodge": 207,
        "attribute_def": 0,
        "attribute_defm": 5,
        "attribute_for": 1,
        "attribute_agi": 1,
        "attribute_vit": 1,
        "attribute_int": 0,
        "attribute_des": 6,
        "attribute_sor": 30,
        "drop_items_id": ["jellopy", "Poring Card"]
    }

def test_not_found_monster_poringao(client):
    response = client.get("/monsters/poringao")
    assert response.status_code == status.HTTP_404_NOT_FOUND
