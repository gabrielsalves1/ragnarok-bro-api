from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def run():
    driver = webdriver.Chrome()

    driver.get('https://playragnarokonlinebr.com/database/thor/itens/detalhes/comp_magic_candy')

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="underlined"]')))

    item_name = driver.find_element(By.XPATH, '//div[@id="itemDescription"]//div//h1').text
    item_img_url = driver.find_element(By.XPATH, f"//img[@alt='{item_name}']").get_attribute('src')
    item_description = driver.find_element(By.XPATH, '//pre').text
    item_price = driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[2]').text
    item_weight = driver.find_element(By.XPATH, '//div[@class="information"]//ul[@class="list"]//li[4]').text

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
            print(f"{info.text} {item_can} \n")

if __name__ == "__main__":
    run()
