from bs4 import BeautifulSoup
import requests
from EksiPack import settings


def get_url_page_count(url):
    response = requests.get(url, headers=settings.HEADERS_GET)
    soup = BeautifulSoup(response.text, 'lxml')
    for page in soup.find_all('div', {'class': 'clearfix sub-title-container'}):
        for el in page.find_all('div', {'class': 'pager'}):
            return int(el["data-pagecount"])