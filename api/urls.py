from . import views
from .views import *
from django.urls import path

urlpatterns = [
    
    path('api/users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',views.Register),
    path('verification/', views.verification),
    path('display/', views.display_users),
    path('forgotpassword/',ForgotPassword.as_view()),
    path('resetpassword_validate/<uidb64>/<token>',views.resetpassword_validate,name="resetpassword_validate"),
    path('resetpassword/',views.resetpassword),
    path('delete/<int>:pk/', views.delete_user),
    
    ]