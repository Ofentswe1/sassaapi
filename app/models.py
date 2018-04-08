from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OfficeAddress(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class CitizenAddress(models.Model):
    id_number = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
