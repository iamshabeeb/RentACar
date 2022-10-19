from email.message import EmailMessage
from random import choices
from django.shortcuts import redirect, render
import razorpay
from rest_framework.response import Response
from payment import serializers

from variations.models import Variation
from .models import Feedback, Order
from rest_framework.decorators import api_view, permission_classes
from .serializers import FeedbackSerializer, PaymentSerializer
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from backend import settings
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# Create your views here.


def payment(request,pk):
    variation = Variation.objects.get(pk = pk)
    payment =0
    order=0
    grand_total = 0
    vanprice = variation.van_items.price
    driverprice = variation.driver_items.price
    guideprice = variation.guide_items.price
    fromdate = variation.from_date
    todate = variation.to_date  
    total = vanprice + driverprice + guideprice
    days = ((todate - fromdate).days)
    grand_total = total * days
    if request.method == 'POST':
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        request.session['key'] = name
        user = variation.user
        print(user,'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        print(name)

        client =razorpay.Client(auth=('rzp_test_VJUYGLcn8bGzW2','RQ60767euGCf8pecC8xxLXme'))
        payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
        print(payment)
      
        user = variation.user
        print(user)
        order = Order.objects.create(variation_id=name, 
                                  order_amount=amount, 
                                  user=user,
                                  order_product = name,
                                  order_id=payment['id'])
        payment['name']=name      
        print(order)      

                                          

    return render(request,'razorpay/razorpay.html',{'payment':payment, 'order':order,'grand_total':grand_total})

def payment_status(request):
    status =None
    response = request.POST

    print("ddd",response)

    params_dict = {
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }

    client =razorpay.Client(auth=('rzp_test_VJUYGLcn8bGzW2','RQ60767euGCf8pecC8xxLXme'))

   
    status = client.utility.verify_payment_signature(params_dict)
    print(status,'ghg')
    try:
        order = Order.objects.get(order_id=response['razorpay_order_id'])
        order.order_payment_id  = response['razorpay_order_id']
        order.razorpay_payment_id  = response['razorpay_payment_id']
            
        order.isPaid = True
        order.order_status='Approved'
        order.save()

        name = request.session['key']
        variation = Variation.objects.get(id=name)
        useri=variation.user.email
        variation.save()

        print(name,111112)
        current_site = 'http://localhost:8000'
        mail_subject = "your payment has been successfull"
        message = render_to_string('razorpay/success-email.html',{
            'user' : request.user,
            'current_site':current_site
        })
        print(message)
        
        to_email = useri
        print(to_email)
        send_mail(mail_subject,message,settings.EMAIL_HOST_USER,[to_email],fail_silently=False)
        print(send_mail,'kkkkkk')
        
        
        return render(request,'razorpay/payment-status.html',{'status':True})
    except:
        return render(request,'razorpay/payment-status.html',{'status':False})



@api_view(['GET'])
def display_order(request):
    order = Order.objects.filter(isPaid=True)
    serializer = PaymentSerializer(order, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def feedback(request,pk):
    data = request.data
    user = request.user
    order = Order.objects.get(pk = pk)
    print(order,'kkkkkkkkkk')
    print(user)
    ispaid = order.isPaid
    print('paid')
    if ispaid == True:
        select = Feedback.objects.create(
            user = user,
            feedback = data['feedback'],
            order = order,

        )
    else:
        return Response('youn are not paid')
    serialiser = FeedbackSerializer(select)

    return Response(serialiser.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def display_feedback(request):
    feedback = Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data)

    
    
    

    
