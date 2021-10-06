import time
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver


URL = "https://www.tury.ru/hotel/most_luxe.php"
#URL = "https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%"
def get_data(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    with open("index_with_hotels.html", "w", encoding='utf-8-sig') as file:
        file.write(r.text)

    # get hotels urls
        r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%", headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        hotels_cards = soup.find_all("div", class_="hotel_card_dv")
    #    print(hotels_cards)


        for hotel_url in hotels_cards:
            hotel_url = hotel_url.find("a").get("href")
            print("https://www.tury.ru" + hotel_url)
get_data(URL)
