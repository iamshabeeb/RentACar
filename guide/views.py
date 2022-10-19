from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from .models import *
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
# Create your views here.

@permission_classes([IsAdminUser])
@api_view(['POST'])
def add_guide(request):
    data = request.data
    guide = Guide.objects.create(
        name = data['name'],
        age = data['age'],
        place = data['place'],
        phone = data['phone'],
        address = data['address'],
        pin = data['pin'],
        experience = data['experience'],
        aadhar_no = data['aadhar_no'],
        price = data['price'],
        is_active = data['is_active']
    )
    serialiser = GuideSerializer(guide)
    return Response(serialiser.data)

@permission_classes([IsAdminUser])
class update_guide(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer





@api_view(['GET'])
def display_guide(request):
    guide = Guide.objects.filter(is_active = True)
    serializer = GuideSerializer(guide, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def booked_guides(request):
    guides = Guide.objects.filter(is_active = False)
    serializer = BookedGuideSerializer(guides, many = True)
    return Response(serializer.data)

