from django.shortcuts import render, redirect
from .models import Car, Comment
from .forms import CarForm, CommentForm
# Create your views here.



def car_list(request):
  cars = Car.objects.all()
  return render(request, 'carsapp/car_list.html', {'cars':cars})

def car_detail(request, pk):
  car = Car.objects.get(id=pk)
  comments = Comment.objects.filter(car=car)
  return render(request, 'carsapp/car_detail.html', {'car': car, 'comments': comments})

def comment_list(request):
  comments = Comment.objects.all()
  return render(request, 'carsapp/comments_list.html',{'comments':comments})

def car_add(request):
  if request.method == "POST":
    form = CarForm(request.POST)
    if form.is_valid():
      car = form.save()
      return redirect('car_detail',pk=car.pk)
  else:
      form = CarForm()

  return render(request, 'carsapp/car_form.html', {'form': form})


def add_car_comment(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.car = car
        new_comment.save()
        return redirect('car_detail', pk=car.pk)
    else:
      form = CommentForm()
    return render(request, 'carsapp/car_detail.html', {'form': form})


def car_detail(request, pk):
  car = Car.objects.get(id=pk)
  comments = Comment.objects.filter(car=car)
  form = CommentForm()
  return render(request, 'carsapp/car_detail.html', {'car': car, 'comments': comments, 'form': form})
