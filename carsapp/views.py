from django.shortcuts import render

# Create your views here.

from .models import Car, Comment

def car_list(request):
  cars = Car.objects.all()
  return render(request, 'carsapp/car_list.html', {'cars',cars})

def car_detail(request,pk):
  car = Car.objects.get(id=pk)
  return render(request, 'carsapp/car_detail.html')

def comment_list(request):
  comments = Comment.objects.all()
  return render(request, 'carsapp/comments_list.html',{'comments',comments})