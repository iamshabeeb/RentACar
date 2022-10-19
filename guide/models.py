from email.policy import default
from django.db import models

# Create your models here.

class Guide(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    place = models.CharField(max_length=50)
    pin = models.IntegerField()
    address = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    aadhar_no = models.BigIntegerField()
    price = models.IntegerField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name