from selenium import webdriver
from item import Item
from monster import Monster
from weapon import Weapon
from equipment import Equipment
from slot import Slot
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    if os.environ['APP_URL'] == 'app':
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Remote('http://selenium:4444/wd/hub', options = options)
    else:
        driver = webdriver.Chrome()

    Item(driver = driver).scraping_items()
    Monster(driver = driver).scraping_monsters()
    Weapon(driver = driver).scraping_weapons()
    Equipment(driver = driver).scraping_equipments()
    Slot(driver = driver).scraping_slots()

    driver.quit()

if __name__ == "__main__":
    main()
