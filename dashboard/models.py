from email.policy import default
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique= True)
    phone_number = models.CharField(max_length=12, unique= True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    status = models.IntegerField(default=False)
