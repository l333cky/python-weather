from http.client import responses

import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    headers = {'Users-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text

def get_weather(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find_all('div', class_='dates short-d')[0].text
    pass

URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
get_weather(html)