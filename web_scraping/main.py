from selenium import webdriver
from item import Item

def run():
    driver = webdriver.Chrome()

    Item(driver = driver).scraping_items()

if __name__ == "__main__":
    run()