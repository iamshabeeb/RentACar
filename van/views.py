from email import message
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser



# Create your views here.

@api_view(['GET'])
def display_van(request):
    van_details = VanDetail.objects.filter(is_active = True)
    serializer = VanDetailSerializer(van_details, many =True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_van(request):
        data = request.data
        vehicle_number = data['vehicle_number']
        if VanDetail.objects.filter(vehicle_number=vehicle_number).exists():
            message ={"error":'Vechile already exist'}
            return Response(message)
        else:    

            van = VanDetail.objects.create(
                van_name = data['van_name'],
                engine = data['engine'],
                overall_length = data['overall_length'],
                overall_height = data['overall_height'],
                fuel_type = data['fuel_type'],
                fuel_capacity = data['fuel_capacity'],
                horse_power = data['horse_power'],
                transmission = data['transmission'],
                injection = data['injection'],
                seating = data['seating'],
                bed = data['bed'],
                washroom = data['washroom'],
                power_supply = data['power_supply'],
                active_brake_assist = data['active_brake_assist'],
                blind_spot_assist_mirror = data['blind_spot_assist_mirror'],
                attension_assist = data['attension_assist'],
                owner_name = data['owner_name'],
                insurance_upto = data['insurance_upto'],
                vehicle_number = vehicle_number,
                status = data['status'],
                fitness_upto = data['fitness_upto'],
                price = data['price'],
            )
            serializer = VanDetailSerializer(van)
            return Response(serializer.data)



@permission_classes([IsAdminUser])
class UpdateVanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=VanDetail.objects.all()
    serializer_class=VanDetailSerializer


@api_view(['GET'])
def booked_vans(request):
    vans = VanDetail.objects.filter(is_active = False)
    serializer = BookedVanSerializer(vans, many = True)
    return Response(serializer.data)


