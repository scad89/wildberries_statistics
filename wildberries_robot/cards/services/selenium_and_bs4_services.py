from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests
import time

options = Options()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
    options=options
)


def price_to_int(soup_price):
    return int(''.join(soup_price.split()))


def getting_data_with_selenium(article):
    url = f'https://www.wildberries.ru/catalog/{article}/detail.aspx'
    try:
        driver.get(url=url)
        time.sleep(3)
        driver.find_element(
            by=By.XPATH, value='//*[@id="infoBlockProductCard"]/div[2]/div/div/p/span')
        soup = BeautifulSoup(driver.page_source, 'lxml')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    return getting_data_with_bs4(soup)


def getting_data_with_bs4(soup):
    actual_price = soup.find(
        'span', class_='price-block__final-price').text.strip().replace('₽', '')
    price_without_discounts = soup.find(
        'del', class_='price-block__old-price').text.strip().replace('₽', '')
    return price_to_int(actual_price), price_to_int(price_without_discounts)


def getting_seller(article):
    url = requests.get(
        f'https://wbx-content-v2.wbstatic.net/sellers/{article}.json')
    return url.json()['supplierName']


def getting_brand_and_name_of_product(article):
    url = requests.get(
        f'https://wbx-content-v2.wbstatic.net/ru/{article}.json')
    return url.json()['selling']['brand_name'], url.json()['imt_name']
