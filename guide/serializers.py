from rest_framework import serializers
from .models import *


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['name', 'age', 'phone', 'place', 'address', 'pin', 'experience', 'aadhar_no', 'price', 'is_active']
        read_only_fields = ['name', 'place', 'address', 'pin', 'aadhar_no']


class BookedGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['name']
