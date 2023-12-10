from selenium import webdriver
from item import Item
from monster import Monster
from weapon import Weapon
from equipment import Equipment
from slot import Slot

def main():
    driver = webdriver.Chrome()

    Item(driver = driver).scraping_items()
    Monster(driver = driver).scraping_monsters()
    Weapon(driver = driver).scraping_weapons()
    Equipment(driver = driver).scraping_equipments()
    Slot(driver = driver).scraping_slots()

if __name__ == "__main__":
    main()
