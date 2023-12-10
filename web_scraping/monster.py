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

class Monster:
    def __init__(self, driver):
        load_dotenv()
        self.driver = driver

    def scraping_monsters(self):
        self.driver.get(f"{os.environ['RAGNAROK_URL']}/database/thor/monstros?page=1")

        WebDriverWait(self.driver, 120).until(ec.presence_of_element_located((By.XPATH, '//h1[text()="Monstros"]')))

        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]').click()
        except:
            pass

        last_page = int(re.search(r"setParam\('page', (\d+)\)", self.driver.find_element(By.XPATH, '//label[@class="box bluebox"]').get_attribute('onclick')).group(1))

        for actual_page in range(2, last_page + 1):
            monsters = self.driver.find_elements(By.XPATH, '//li[@class="monstros show"]//a')

            for monster in monsters:
                monster_url = monster.get_attribute('href')

                self.scraping_and_post(url = monster_url)

                self.driver.back()

            self.driver.get(f"{os.environ['RAGNAROK_URL']}/database/thor/monstros?page={actual_page}")

    def scraping_and_post(self, url):
        data = {}

        self.driver.get(url)

        WebDriverWait(self.driver, 120).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="underlined"]')))

        data['id'] = str(re.search(r'/detalhes/(\w+)', url).group(1))
        data['name'] = self.driver.find_element(By.XPATH, '//div[@id="itemDescription"]//div//h1').text
        data['level'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[2]').text))
        data['race'] = self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[4]').text
        data['monster_property'] = self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[6]').text
        data['size'] = self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[8]').text
        data['base_exp'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[10]').text))
        data['class_exp'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//ul[@id="informacoes-list"]//li[12]').text))

        try:
            data['img_url'] = self.driver.find_element(By.XPATH, '//div[@id="hidden"]//img[@id="monster"]').get_attribute('src')
        except:
            data['img_url'] = 'https://playragnarokonlinebr.com/database/img/resultado/Monstros/icon.png'

        data['resistence_neutral'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text))
        data['resistence_water'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[4]').text))
        data['resistence_earth'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[6]').text))
        data['resistence_fire'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[8]').text))
        data['resistence_wind'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[10]').text))
        data['resistence_poison'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[12]').text))
        data['resistence_holy'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[14]').text))
        data['resistence_dark'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[16]').text))
        data['resistence_ghost'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[18]').text))
        data['resistence_curse'] = 0 if self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[2]').text == '-' else int(re.sub(r'\%', '', self.driver.find_element(By.XPATH, '//ul[@id="property"]//li[20]').text))

        data['hp'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@class="information"]//ul[@class="list"]//li[2]').text))

        attack = self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@class="information"]//ul[@class="list"]//li[4]').text
        text_without_dot = re.sub(r'\.', '', attack)
        text_numbers = re.findall(r'\b(\d+)\b', text_without_dot)
        numbers = [int(number) for number in text_numbers]

        data['attack_min'] = numbers[0]
        data['attack_max'] = numbers[1]
        data['attack_range'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@class="information"]//ul[@class="list"]//li[6]').text))
        data['precision'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@class="information"]//ul[@class="list"]//li[8]').text))
        data['dodge'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@class="information"]//ul[@class="list"]//li[10]').text))

        data['attribute_def'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[2]').text))
        data['attribute_vit'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[4]').text))
        data['attribute_defm'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[6]').text))
        data['attribute_int'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[8]').text))
        data['attribute_for'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[10]').text))
        data['attribute_des'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[12]').text))
        data['attribute_agi'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[14]').text))
        data['attribute_sor'] = int(re.sub(r'\.', '', self.driver.find_element(By.XPATH, '//div[@id="two-flexbox"]//div[@id="flex-outside"]//ul//li[16]').text))

        self.driver.find_element(By.XPATH, '//div[@class="slick-track"]//li[1]').click()

        drop_items = self.driver.find_elements(By.XPATH, '//li[@class="itens show"]//a')

        items_id = []
        for item in drop_items:
            items_id.append(str(re.search(r'/detalhes/(\w+)', item.get_attribute('href')).group(1)))

        data['drop_items_id'] = items_id

        response = requests.post(f"http://{os.environ['APP_URL']}:{int(os.environ['APP_PORT'])}/monsters", data=json.dumps(data))

        if response.status_code == 409:
            response = requests.put(f"http://{os.environ['APP_URL']}:{int(os.environ['APP_PORT'])}/monsters/{data['id']}", data=json.dumps(data))

        print(response)

