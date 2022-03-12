from unicodedata import name
from django.shortcuts import render
from core.models import Crypto, CryptoPrice

def index(request):
    
    name = Crypto.objects.get(name='Bitcoin')
    prices = CryptoPrice.objects.filter(crypto=name)

    context = {'currency': name, 'crypto_prices': prices}
    return render(request, 'index.html', context)
