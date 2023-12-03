from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import re
from dotenv import load_dotenv
import os
import requests
import json

class Item:
    def __init__(self, driver):
        self.driver = driver

    def scraping_items(self):
        self.driver.get('https://playragnarokonlinebr.com/database/thor/itens')

        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, '//h1[text()="Itens"]')))

        last_page = int(re.search(r"setParam\('page', (\d+)\)", self.driver.find_element(By.XPATH, '//label[@class="box bluebox"]').get_attribute('onclick')).group(1))

        for actual_page in range(1, last_page + 1):
            items = self.driver.find_elements(By.XPATH, '//li[@class="itens show"]//a')

            for item in items:
                item_url = item.get_attribute('href')

                self.scraping_and_post(url = item_url)

                self.driver.back()

            self.driver.get(f"https://playragnarokonlinebr.com/database/thor/itens?page={actual_page}")

    def scraping_and_post(self, url):
        data = {}

        self.driver.get(url)

        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="underlined"]')))

        data['id'] = str(re.search(r'/detalhes/(\w+)', url).group(1))
        data['name'] = self.driver.find_element(By.XPATH, '//div[@id="itemDescription"]//div//h1').text
        data['img_url'] = self.driver.find_element(By.XPATH, f"//img[@alt='{data['name']}']").get_attribute('src')
        data['description'] = self.driver.find_element(By.XPATH, '//pre').text
        data['price'] = int(''.join(filter(str.isdigit, self.driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[2]').text)))
        data['weight'] = self.driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[4]').text

        item_informations = self.driver.find_elements(By.XPATH, '//div[@id="more-information"]//ul[@class="flex-check"]//li')

        count = 0
        item_can = False
        for info in item_informations:
            count += 1

            if info.text == '':
                item_can_url = self.driver.find_element(By.XPATH, f"//div[@id='more-information']//ul[@class='flex-check']//li[{count}]//img").get_attribute('src')

                if 'NEGATIVE' in item_can_url:
                    item_can = False
                elif 'POSITIVE' in item_can_url:
                    item_can = True

                continue

            if (count % 2) == 0:
                match info.text:
                    case 'Jogado no chão':
                        data['thrown_on_the_floor'] = item_can
                    case 'Negociado':
                        data['negotiated'] = item_can
                    case 'Colocado no armazém':
                        data['placed_in_the_warehouse'] = item_can
                    case 'Guardado no carrinho':
                        data['stored_in_cart'] = item_can
                    case 'Vendido para NPC':
                        data['sold_to_npc'] = item_can
                    case 'Colocado no armazém da guilda':
                        data['placed_in_the_guild_warehouse'] = item_can

        load_dotenv()

        response = requests.post(f"http://{os.environ['APP_URL']}:{int(os.environ['APP_PORT'])}/items", data=json.dumps(data))
        print(response.text)
