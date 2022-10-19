from rest_framework import serializers

from van.models import VanDetail
from .models import *

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['name', 'age', 'place', 'phone', 'pin', 'address', 'experience', 'license_no','aadhar_no', 'price', 'is_active']
        read_only_fields = ['name', 'place', 'pin', 'license_no', 'aadhar_no']


class BookedDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['name']