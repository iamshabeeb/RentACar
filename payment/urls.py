from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/',views.payment, name='payment'),
    path('status/', views.payment_status,name='payment-status'),
    path('display/', views.display_order),
    path('feedback/<int:pk>/', views.feedback),
    path('display_feedback/', views.display_feedback)
]
