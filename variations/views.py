from lib2to3.pgen2.driver import Driver
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Variation
from driver.models import Drivers
from guide.models import Guide
from van.models import VanDetail
from .serializers import DisplayVariations, VariationSerializer
from rest_framework.response import Response
from datetime import datetime,timedelta

# Create your views here.

# 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def variations(request):
    data = request.data
    user = request.user
    select = Variation.objects.create(
        user=user,   
        van_items_id = data['van_items'],
        driver_items_id = data['driver_items'],
        guide_items_id = data['guide_items'],
        from_date = data['from_date'],
        to_date = data['to_date'],
    )

    
    serializer = VariationSerializer(select)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def display_order(request):
    order = Variation.objects.all()
    serialiser = DisplayVariations(order,many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def calculation(request, pk):
    variation = Variation.objects.get(pk = pk)
    vanprice =variation.van_items.price
    driverprice = variation.driver_items.price
    guideprice = variation.guide_items.price
    fromdate = variation.from_date
    todate = variation.to_date
    van = variation.van_items_id
    driver = variation.driver_items_id
    guide = variation.guide_items_id
    total = vanprice + driverprice + guideprice
    days = ((todate - fromdate).days)
    grand_total = total * days
    print(van,"ff")
    formdata={
        'driverprice':driverprice,
        'vanprice':vanprice,
        'guideprice':guideprice,
        'fromdate': fromdate,
        'todate': todate,
        'total':total,
        'days':days,
        'van':van,
        'driver':driver,
        'guide':guide,
        'grand_total':grand_total
    }
    date_format = "%Y/%m/%d"
    start = datetime.strftime(fromdate,date_format)
    print('from', start)
    end = datetime.strftime(todate,date_format)
    print('end', end)
    now = datetime.now().strftime('%Y/%m/%d')
    print('now',now)

    if end < now:
        # event in past
        vans =VanDetail.objects.get(id=van)
        vans.is_active = True
        vans.save()
        drivers = Drivers.objects.get(id=driver)
        drivers.is_active = True
        drivers.save()
        guides = Guide.objects.get(id=guide)
        guides.is_active = True
        guides.save()
        
        print('past')
    elif start > now:
        # event in future
        vans =VanDetail.objects.get(id=van)
        vans.is_active = True
        vans.save()
        drivers = Drivers.objects.get(id=driver)
        drivers.is_active = True
        drivers.save()
        guides = Guide.objects.get(id=guide)
        guides.is_active = True
        guides.save()
        print('future')
        
    else:
        # event occuring now
        vans =VanDetail.objects.get(id=van)
        vans.is_active = False
        vans.save()
        drivers = Drivers.objects.get(id=driver)
        drivers.is_active = False
        drivers.save()
        guides = Guide.objects.get(id=guide)
        guides.is_active = False
        guides.save()
        print('now')
    
    
    return Response(formdata)









    

    

