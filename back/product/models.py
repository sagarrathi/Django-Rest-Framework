from email import contentmanager
from turtle import mode
from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120, blank=True, null=True) 
    price=models.DecimalField(max_digits=12, decimal_places=2, default=99.99)
