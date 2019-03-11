from EksiPack import settings
from EksiPack.get_page_number_of_topic import get_url_page_count
from EksiPack.time_parser import time_parser
from EksiPack.text_extractor import extractor
import requests
from bs4 import BeautifulSoup

class EksiInformation:
    def __init__(self):
        pass

    def get_url_response_text(self,url):
        response = requests.get(url, headers=settings.HEADERS_GET)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_topic_information(self,url,page_required = 2):
        if page_required == 0: # default olarak sadece ilk page döner, eğer sıfır verirseniz hepsi döner
            page_required = get_url_page_count(url)

        elif page_required == 1:
            page_required = 2

        entry_list = []
        for page_no in range(page_required,1, -1 ): # tersten başla 1 e kadar gel
            soup = self.get_url_response_text(url+"?p={}".format(page_no))
            for link in soup.find_all('div', {'class': 'info'}):
                for entry_date in link.find_all('a', {'class': 'entry-date permalink'}):
                    try:
                        eksi_entry_time = time_parser(entry_date.get_text())
                        datetime_to_str = eksi_entry_time.strftime(settings.DATE_FORMAT)
                    except:
                        datetime_to_str = "01.01.1999 00:00"
                    for entry_author in link.find_all('a', {'class': 'entry-author'}):
                        entry_url = settings.EKSI_BASE_URL + entry_date['href']
                        entry_list.append({
                            "author": entry_author.get_text(),
                            "publish_date": datetime_to_str,
                            "entry_url": entry_url,
                            "text": extractor(entry_url)
                        })
                    else:
                        continue
        return entry_list