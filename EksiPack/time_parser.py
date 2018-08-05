from EksiPack import settings
from datetime import datetime

def time_parser(eksi_time):
    '''
    Tarih+saat 16 karakter bununla birlikte,
    bu " ~ " karakterden sonra birinci elemanda 16 (exp=> 23.12.2023 22:15)
    karakter varsa str to time yapılır.
    16 karakterden az olursa bunun anlamı o entry o gün içerisinde değiştirilmiş
    yani sadece 5 karakteri var oda saat ve işareti (exp=> 15:15)
    fakat burada gün içerisinde degismesine karşın tarihi bulunmamakta
    bu sebepten dolayı sıfırıncı elemanın tarihi alınıp eklenir tekrar str to time yapılır.
    '''
    if settings.EKSI_SPECIFIC_CHAR in eksi_time:
        if len(eksi_time.split(settings.EKSI_SPECIFIC_CHAR)[1]) == settings.LEN_EKSI_DATE:
            time_parser = (eksi_time.split(settings.EKSI_SPECIFIC_CHAR)[1])
            str_to_time_h = datetime.strptime(time_parser, settings.DATE_FORMAT)

        else:
            time_parser = (eksi_time.split(" ")[0] + " " + eksi_time.split(settings.EKSI_SPECIFIC_CHAR)[1])
            str_to_time_h = datetime.strptime(time_parser, settings.DATE_FORMAT)

        return str_to_time_h

    else:
        str_to_time = datetime.strptime(eksi_time, settings.DATE_FORMAT)
        return str_to_time
