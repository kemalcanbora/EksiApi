HOST = "https://api.eksisozluk.com"

login_headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/2.3.0',
}

proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

TOR_PASSWORD = "my password"

DATA = dict(grant_type='password',
            username='eksi_sozlukte_kullandigin@mail.com',
            password='eksi_password',
            client_secret='6cba2458-6fa8-4c55-8d72-78620542e43d')