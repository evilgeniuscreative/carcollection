from django.urls import path
from . import views

urlpatterns = [
  path('', views.car_list, name='car_list'),
  path('cars/<int:pk>', views.car_detail, name='car_detail'),
  path('cars/add/', views.car_add, name='car_add'),
  path('cars/<int:pk>/comment/', views.add_car_comment, name='add_car_comment'),
  path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
  path('cars/<int:pk>/delete', views.car_delete, name='car_delete'),
  path('signout/', views.signout, name='signout'),
  path('signin/', views.signin, name='signin'),
  path('signup/', views.signup, name='signup'),
  path('cars/<int:pk>/add_to_collection', views.add_to_collection, name='add_to_collection'),
]