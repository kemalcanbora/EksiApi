### EksiApi

 Ekşi is a collaborative hypertext "dictionary" based on the concept of Web sites built up on user contribution.<br>

 However, Ekşi Sözlük is not a dictionary in the strict sense; users are not required to write correct information. It is currently one of the largest online communities in Turkey with over 400,000 registered users.<br>
 
The number of writers is about 54,000. As an online public sphere, 
 Ekşi Sozluk is not only utilized by thousands for information sharing on various topics ranging from scientific subjects to everyday life issues, but also used as a virtual socio-political community to communicate disputed political contents and to share personal views.


### How can I use it?
- Change settings file with your email and password.
- <b>get_populer_topics</b> : You can view popular topics.
- <b>get_entry_with_entry_id</b> : You can see the information of the entry.
- <b>get_topic_with_topic_id</b> : You can see the information of the topic.
- If you want to use proxy;
``` shell
docker-compose up
```
Example with proxy:
``` Python
from EksiPack.v1.app import EksiApi

eksi = EksiApi(proxy_val=True)
populer_info = eksi.get_populer_topics()

# output : {'Topics': [{'MatchedCount': 212, 'TopicId': 6904055, 'FullCount': 213, 'Title': "erdoğan'ın tabldot yemek yemesi"}, 
#                      {'MatchedCount': 187, 'TopicId': 6904027, 'FullCount': 189, 'Title': 'ikizderelilerin bize destek verin çağrısı'}, 
#                      {'MatchedCount': 57, 'TopicId': 6904040, 'FullCount': 57, 'Title': '3 mayıs 2021 metropoll araştırma z kuşağı tercihi'}]

```

### Problems
- You can use ```time.sleep()``` between queries. Because sometimes it returns ```None```.

### It is not an Official API.

