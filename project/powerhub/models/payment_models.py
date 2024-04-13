from django.db import models
from .auth_models import User, QueekaBusiness

class VirtualCard(models.Model):
    business = models.OneToOneField(QueekaBusiness, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=50, unique=True)
    account_id = models.CharField(max_length=35, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.business.name


