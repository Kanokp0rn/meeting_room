from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('book/', views.booking_create, name='booking_create'),
    path('edit/<int:pk>/', views.booking_create, name='booking_edit'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),
]