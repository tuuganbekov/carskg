import requests
from bs4 import BeautifulSoup
import json
from db_connect import *

URL = 'https://cars.kg/offers?direction=sale&vendor=57fa24ee2860c45a2a2c0905&model=58b876792860c409036ea149&generation=&price_from=&price_to=&year_from=&year_to=2021&running_length_from=&running_length_to=&kuzov=&capacity_from=&capacity_to=&color=&city='
LINK = 'https://www.cars.kg/'
HEADERS = {
    "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    "accept": '*/*',
}


def get_html(url, params=None):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a', class_='catalog-list-item')

    cars = []

    for item in items:
        cars.append({
            "name": item.find('span', class_='catalog-item-caption').get_text()
                .replace('\n', '').replace('            ', ''),
            "description": item.find('span', class_='catalog-item-descr').get_text()
                .replace('\n', '').replace('                                    ', '').replace('    ', ' '),
            "image_link": item.find('img', class_='catalog-item-cover-img')['src'],
            "price_usd": item.find('span', class_="catalog-item-price").get_text().replace('$ ', ""),
            "link": LINK + item['href'],
            "mileage": item.find('span', class_='catalog-item-mileage').get_text().replace(' км', '')
            if item.find('span', class_='catalog-item-mileage').get_text().replace(' км', '') != '' else "0",
            "year": item.find('span', class_='caption-year').get_text(),
        })

    return cars


def return_json(cars):
    with open('cars.json', 'w') as file:
        json.dump(cars, file, ensure_ascii=False, indent=3)


def write_to_db(cars):
    for item in cars:
        item = Car(name=item['name'], description=item['description'], year=item['year'], mileage=item['mileage'],
                   price_usd=item['price_usd'], image_link=item['image_link'], link=item['link'])

        item.save()


def parse():
    html = get_html(URL)
    get_content(html)
    cars = get_content(html)
    write_to_db(cars)
    return_json(cars)


parse()
