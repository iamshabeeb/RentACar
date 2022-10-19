from . import views
from .views import *
from django.urls import path

urlpatterns = [
    
    path('add/', views.add_guide),
    path('update/<int:pk>/', views.update_guide.as_view()),
    path('display/', views.display_guide),
    path('delete/<int:pk>/', views.update_guide.as_view()),
    path('booked/', views.booked_guides),
    
    ]