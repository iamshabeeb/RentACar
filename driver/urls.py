from . import views
from .views import *
from django.urls import path

urlpatterns = [
    
    path('add/', views.add_drivers),
    path('display/', views.display_drivers),
    path('update/<int:pk>/', views.updata_driver.as_view()),
    path('delete/<int:pk>/', views.updata_driver.as_view()),
    path('booked/', views.booked_drivers),

    ]