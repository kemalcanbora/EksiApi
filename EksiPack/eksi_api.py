from EksiPack.get_category_topics import get_links_to_the_category
from EksiPack.get_topic_entry_and_others import EksiInformation

class EksiApi:
    def __init__(self):
        pass

    def get_category_topics(self,category):
        '''settings de bulunmakta'''
        return get_links_to_the_category(category_url=category)

    def get_url_informations(self,url,date=None):
        '''date type : YYYY-MM-DD sadece bu tarihte bulunan entryleri getirir.Default olarak baştan sona getir dedim
            fakat burada söyle bir problem var üzerine çok fazla yazılan konularda sıkıntı büyük.'''

        if date is not None:
            url = url+"?day=".format(date)
        return EksiInformation().get_topic_information(url)
