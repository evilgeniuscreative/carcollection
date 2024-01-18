from django.urls import path
from . import views

urlpatterns = [
  path('', views.car_list, name='car_list'),
  path('cars/<int:pk>', views.car_detail, name='car_detail'),
  path('cars/add/', views.car_add, name='car_add')
]