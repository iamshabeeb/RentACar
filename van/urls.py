from . import views
from .views import *
from django.urls import path

urlpatterns = [
    
    path('display/', views.display_van),
    path('add/', views.add_van),
    path('update/<int:pk>/', views.UpdateVanDetail.as_view()),
    path('delete/<int:pk>/', views.UpdateVanDetail.as_view()),
    path('booked/', views.booked_vans),
    
    ]