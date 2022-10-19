from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *



class VanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VanDetail
        
        fields = ['van_name', 'engine', 'overall_length', 'overall_height', 'fuel_type', 'fuel_capacity', 'horse_power',
                  'transmission', 'injection', 'seating', 'bed', 'washroom', 'power_supply', 'active_brake_assist', 
                  'blind_spot_assist_mirror', 'attension_assist', 'owner_name', 'insurance_upto', 'vehicle_number', 
                  'price', 'status','is_active']
        read_only_fields = ['van_name', 'engine', 'overall_length', 'overall_height', 'fuel_type', 'fuel_capacity', 'horse_power',
                  'transmission', 'injection', 'seating', 'bed', 'washroom', 'power_supply', 'active_brake_assist', 
                  'blind_spot_assist_mirror', 'attension_assist', 'owner_name', 'insurance_upto', 'vehicle_number',]


class BookedVanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VanDetail
        fields = ['van_name']