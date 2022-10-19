from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.

class Drivers(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    pin = models.IntegerField()
    address = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50)
    aadhar_no = models.BigIntegerField()
    price = models.IntegerField() 
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name