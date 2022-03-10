from django.db import models

# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class CryptoPrice(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name='prices')
    price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.crypto.name} - {self.price}'
