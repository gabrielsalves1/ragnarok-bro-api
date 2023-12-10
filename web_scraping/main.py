from selenium import webdriver
from item import Item
from monster import Monster
from weapon import Weapon

def main():
    driver = webdriver.Chrome()

    Item(driver = driver).scraping_items()
    Monster(driver = driver).scraping_monsters()
    Weapon(driver = driver).scraping_weapons()

if __name__ == "__main__":
    main()
