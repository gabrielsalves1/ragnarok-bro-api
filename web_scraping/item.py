from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import requests
import json

class Item:
    def scraping_and_post_item(driver, url):
        data = {}

        driver.get(url)

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="underlined"]')))

        data['id'] = 'comp_magic_candy'
        data['name'] = driver.find_element(By.XPATH, '//div[@id="itemDescription"]//div//h1').text
        data['img_url'] = driver.find_element(By.XPATH, f"//img[@alt='{data['name']}']").get_attribute('src')
        data['description'] = driver.find_element(By.XPATH, '//pre').text
        data['price'] = int(''.join(filter(str.isdigit, driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[2]').text)))
        data['weight'] = driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[4]').text

        item_informations = driver.find_elements(By.XPATH, '//div[@id="more-information"]//ul[@class="flex-check"]//li')

        count = 0
        item_can = False
        for info in item_informations:
            count += 1

            if info.text == '':
                item_can_url = driver.find_element(By.XPATH, f"//div[@id='more-information']//ul[@class='flex-check']//li[{count}]//img").get_attribute('src')

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

        response = requests.post('http://127.0.0.1:8000/items', data=json.dumps(data))
        print(response.text)
