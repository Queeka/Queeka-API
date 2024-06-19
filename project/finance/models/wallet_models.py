from django.db import models
from . import QueekaBusiness

class BusinessWallet(models.Model):
    business = models.ForeignKey(QueekaBusiness, on_delete=models.CASCADE)
    nuban = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=400)
    balance = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.business.name