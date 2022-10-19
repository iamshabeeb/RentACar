from django.urls import path
from . import views
from .views import variations

urlpatterns = [

    path('select/', views.variations),
    path('display/', views.display_order),
    path('calculate/<int:pk>/', views.calculation),

]
