from django.db import models
from api.models import Account
from van.models import VanDetail
from driver.models import Drivers
from guide.models import Guide
# Create your models here.

class Variation(models.Model):
    user = models.ForeignKey(Account, on_delete = models.CASCADE)
    van_items = models.ForeignKey(VanDetail, on_delete = models.CASCADE)
    driver_items = models.ForeignKey(Drivers, on_delete = models.CASCADE, null = True,blank=True)
    guide_items = models.ForeignKey(Guide, on_delete = models.CASCADE, null = True,blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    


    