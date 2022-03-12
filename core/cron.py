from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from django.conf import settings
import requests
from core.models import Crypto, CryptoPrice

def fetch_price():
    headers = {
        "X-CMC_PRO_API_KEY": settings.COIN_MARKET_API_KEY
    }
    response = requests.get(settings.API_URL, headers = headers)
    data = response.json()["data"]

    for currency in data:
        name = currency["name"]
        symbol = currency["symbol"]
        price = currency["quote"]["USD"]["price"]

        print(name, symbol, price)

        crypto = Crypto.objects.get_or_create(name=name, symbol=symbol)[0]

        CryptoPrice.objects.create(crypto=crypto, price=price)

