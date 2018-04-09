from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OfficeAddress(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class CitizenAddress(models.Model):
    username = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Payments(models.Model):
    username = models.CharField(max_length=13)
    balance = models.FloatField()
    pay_date = models.DateField()
    collected = models.CharField(max_length=3)
    collected_date = models.DateTimeField()
