from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import re
from dotenv import load_dotenv
import os
import requests
import json
import time

class Equipment:
    def __init__(self, driver):
        load_dotenv()
        self.driver = driver

    def scraping_equipments(self):
        self.driver.get(f"{os.environ['RAGNAROK_URL']}/database/thor/equipamentos?page=1")

        WebDriverWait(self.driver, 120).until(ec.presence_of_element_located((By.XPATH, '//h1[text()="Equipamentos"]')))

        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]').click()
        except:
            pass

        last_page = int(re.search(r"setParam\('page', (\d+)\)", self.driver.find_element(By.XPATH, '//label[@class="box bluebox"]').get_attribute('onclick')).group(1))

        for actual_page in range(2, last_page + 1):
            items = self.driver.find_elements(By.XPATH, '//li[@class="equipamentos show"]//a')

            for item in items:
                item_url = item.get_attribute('href')

                self.scraping_and_post(url = item_url)

                self.driver.back()

            self.driver.get(f"{os.environ['RAGNAROK_URL']}/database/thor/equipamentos?page={actual_page}")

    def scraping_and_post(self, url):
        data = {}

        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="underlined"]')))
        except:
            return

        data['id'] = str(re.search(r'/detalhes/(\w+)', url).group(1))
        data['name'] = self.driver.find_element(By.XPATH, '//div[@id="itemDescription"]//div//h1').text
        data['description'] = self.driver.find_element(By.XPATH, '//pre').text
        data['price'] = int(''.join(filter(str.isdigit, self.driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[2]').text)))
        data['weight'] = self.driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[4]').text

        try:
            data['img_url'] = self.driver.find_element(By.XPATH, '//div[@class="item-img"]//img').get_attribute('src')
        except:
            data['img_url'] = 'https://playragnarokonlinebr.com/database/img/resultado/Itens/icon.png'

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

        self.driver.find_element(By.XPATH, '//div[@class="slick-track"]//li[1]').click()
        drop_from = self.driver.find_elements(By.XPATH, '//li[@class="monstros show"]//a')
        monsters_id = []
        for monster in drop_from:
            monsters_id.append(str(re.search(r'/detalhes/(\w+)', monster.get_attribute('href')).group(1)))
        data['drop_from_monster_id'] = monsters_id

        self.driver.find_element(By.XPATH, '//div[@class="slick-track"]//li[2]').click()
        obtained_from = self.driver.find_elements(By.XPATH, '//li[@class="itens show"]//a')
        obtained_from_id = []
        for obtained in obtained_from:
            obtained_from_id.append(str(re.search(r'/detalhes/(\w+)', obtained.get_attribute('href')).group(1)))
        data['obtained_from_id'] = obtained_from_id

        response = requests.post(f"http://{os.environ['APP_URL']}:{int(os.environ['APP_PORT'])}/equipments", data=json.dumps(data))

        if response.status_code == 409:
            response = requests.put(f"http://{os.environ['APP_URL']}:{int(os.environ['APP_PORT'])}/equipments/{data['id']}", data=json.dumps(data))

        print(response)
