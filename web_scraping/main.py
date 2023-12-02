from selenium import webdriver
from web_scraping.item import Item

def run():
    driver = webdriver.Chrome()

    Item.scraping_and_post_item(driver = driver, url = 'https://playragnarokonlinebr.com/database/thor/itens/detalhes/comp_magic_candy')

if __name__ == "__main__":
    run()