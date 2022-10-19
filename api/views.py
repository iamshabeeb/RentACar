from urllib import request
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .verify import send, check
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from . serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from rest_framework.views import APIView

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import render


from .models import Account

@api_view(['POST'])
def Register(request):
    try:
        data=request.data
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        password=data['password']
        confirm_password=data['confirm_password']
        phone=data['phone']

        if email=='' or first_name=='' or last_name ==''  or password=='' or confirm_password=='' or phone=='':
            message={'error':' fill the blanks','status':'false'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        if password!=confirm_password:
            message={'error':'password missmatch','status':'false'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)    
        else:
            userpassword = password


        users=Account()
        users.first_name=first_name
        users.last_name=last_name
        users.email=email
        users.password=make_password(userpassword)
        users.phone=phone
        users.save()
        send(phone)
        phone = data['phone']
        request.session['phone'] = phone

        serilaizer = AccountSerilaizer(users, many=False)
        return Response(serilaizer.data,status=status.HTTP_200_OK)


    except:
        message = {'detail': 'User with this email already exist','status':'false'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verification(request):
    try:
        data = request.data
        phone = data['phone']
        code = data['code']
        if check(phone, code):
            user = Account.objects.get(phone=phone)
            user.is_active = True
            user.save()
            serializer=AccountSerilaizer(user,many=False)
            return Response(serializer.data)
        else:
            message={'detail':'otp is not valid'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)    
    except:
        message={'detail':'error in serializer'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['firstname'] = self.user.first_name
        data['email'] = self.user.email

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def display_users(request):
    user = Account.objects.all()
    serialiser = AccountSerilaizer(user, many=True)
    return Response(serialiser.data)



class ForgotPassword(APIView):
    def post(self,request):
        data = request.data
        
        email = data['email']
        
        if Account .objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

        #reset password mail

            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            email = email
            message={f'detail':'Password reset link is send to your email'}
            return Response(message,status=status.HTTP_200_OK)

        else:
                message={'detail':'no account presented'}
                return Response(message,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def resetpassword_validate(request, uidb64, token): 
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Account._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            request.session['uid'] = uid
            message={'detail':'uid taken'}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message={'detail':'no account presented'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def resetpassword(request):
    data = request.data
    print(data)
    create_password = data['create_password']     
    confirm_password = data['confirm_password'] 
    print(create_password)        

    if create_password == confirm_password:

        uid = request.session.get('uid')
        user = Account.objects.get(pk=uid)
        user.set_password(create_password)
        user.save()
        message={'message':'password reset successfully'}
        return Response(message,status=status.HTTP_200_OK)
    else:
            message={'message':'password not match'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)



@permission_classes
class delete_user(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerilaizer

    





