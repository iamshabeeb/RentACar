from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *




class AccountSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields =['first_name','last_name','password','email','phone']

















 


