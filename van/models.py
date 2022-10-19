from django.db import models

# Create your models here.



class VanDetail(models.Model):
    van_name = models.CharField(max_length=50)
    overall_length = models.CharField(max_length=20)
    overall_height = models.CharField(max_length=20)
    engine = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    fuel_capacity = models.CharField(max_length=50)
    horse_power = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    injection = models.CharField(max_length=50)
    seating = models.IntegerField()
    bed = models.IntegerField()
    owner_name = models.CharField(max_length=50)
    insurance_upto = models.CharField(max_length=50)
    fitness_upto = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=50)
    price = models.IntegerField()
    washroom = models.BooleanField(default=False)
    power_supply = models.BooleanField(default=False)
    active_brake_assist = models.BooleanField(default=False)
    blind_spot_assist_mirror = models.BooleanField(default=False)
    attension_assist = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return self.van_name
