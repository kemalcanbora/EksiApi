import requests
from EksiPack.settings import HOST, DATA, login_headers, TOR_PASSWORD, proxies
from EksiPack.v1.route.routes import Routes
from stem.control import Controller
from stem import Signal


class EksiApi:
    def __init__(self, proxy_val=False):
        self.popular = Routes.popular
        self.token = Routes.token
        self.entry = Routes.entry
        self.topic = Routes.topic
        self.proxy_val = proxy_val

    def renew_tor(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
            controller.close()

    def get_session(self):
        session = requests.session()
        session.headers = login_headers
        r = session.get(HOST + "/token", data=DATA, proxies=proxies)
        if r.status_code == 200:
            session.headers['authorization'] = "bearer " + r.json()['access_token']
            return session
        else:
            return False

    def get_populer_topics(self):
        if self.get_session() != False:
            data = self.get_session().get(HOST + self.popular, proxies=proxies).json()
            if (data == None and self.proxy_val):
                self.renew_tor()
            else:
                return data

    def get_entry_with_entry_id(self, entry_id: str):
        if self.get_session() != False:
            data = self.get_session().get(HOST + self.entry.format(entry_id), proxies=proxies).json()
            if (data == None and self.proxy_val):
                self.renew_tor()
            else:
                return data

    def get_topic_with_topic_id(self, topic_id: str):
        if self.get_session() != False:
            data = self.get_session().get(HOST + self.topic.format(topic_id), proxies=proxies).json()
            if (data == None and self.proxy_val):
                self.renew_tor()
            else:
                return data
