from django.db import models
from .product import Product
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default="", blank=True)
    phone = models.CharField(max_length=30, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

