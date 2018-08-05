from EksiPack.eksi_api import EksiApi

info = EksiApi().get_url_informations(url="https://eksisozluk.com/ogrenildiginde-ufku-iki-katina-cikaran-seyler--2593151")
print(info)