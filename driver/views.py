from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_drivers(request):
    data = request.data
    driver = Drivers.objects.create(
        name = data['name'],
        age = data['age'],
        place = data['place'],
        phone = data['phone'],
        price = data['price'],
        pin = data['pin'],
        address = data['address'],
        experience = data['experience'],
        license_no = data['license_no'],
        aadhar_no = data['aadhar_no'],
        is_active = data['is_active'],
    )
    serialiser = DriverSerializer(data)
    return Response(serialiser.data)


@api_view(['GET'])
def display_drivers(request):
    drivers = Drivers.objects.filter(is_active = True)
    print(drivers)
    serializer = DriverSerializer(drivers, many = True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
class updata_driver(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriverSerializer


@api_view(['GET'])
def booked_drivers(request):
    drivers = Drivers.objects.filter(is_active = False)
    serializer = BookedDriverSerializer(drivers, many = True)
    return Response(serializer.data)



