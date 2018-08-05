from bs4 import BeautifulSoup
import requests
import ssl
from EksiPack import settings

ssl._create_default_https_context = ssl._create_unverified_context
url_list = []

def get_links_to_the_category(category_url):
    response = requests.get(category_url, headers=settings.HEADERS_GET)
    while response.status_code != settings.HTTP_OK:
        response = requests.get(category_url, headers=settings.HEADERS_GET)
    if response.status_code == settings.HTTP_OK:
        soup = BeautifulSoup(response.text, 'lxml')
        for url_in_xml in soup.find_all('div',{"class":"instapaper_body"}):
            for link in url_in_xml.find_all("a",href=True):
                split_link = (link["href"].split("?day"))
                url_list.append(settings.EKSI_BASE_URL + split_link[0])

    return url_list[:-1] # -1 olma sebebi sonuncu link page 2 ye gidiyor