from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Comment
from .forms import CarForm, CommentForm
# Create your views here.


# LOGIN


# CARS

def car_list(request):
  cars = Car.objects.all()
  return render(request, 'carsapp/car_list.html', {'cars':cars})

def car_detail(request, pk):
  car = Car.objects.get(id=pk)
  comments = Comment.objects.filter(car=car)
  form = CommentForm()
  return render(request, 'carsapp/car_detail.html', {'car': car, 'comments': comments, 'form': form})

def car_edit(request, pk):
    car =  Car.objects.get(id=pk)

    if request.method == 'POST':
      form = CarForm(request.POST, instance=car)
      if form.is_valid():
        car = form.save()
        return redirect('car_detail', pk=car.pk)
    else:
      form = CarForm(instance=car)

    return render(request, 'carsapp/car_form.html', {'form': form})

def car_delete(_, pk):
    car = Car.objects.get(id=pk)
    car.delete()
    return redirect('car_list')


# COMMENTS 
@login_required
def add_car_comment(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.car = car
        new_comment.user = request.user  
        new_comment.save()
        return redirect('car_detail', pk=car.pk)
    else:
      form = CommentForm()
    return render(request, 'carsapp/car_detail.html', {'form': form, 'car':car},)

# TODO: Edit comment, delete comment

# in car_detail
  # check if authenticated
  # Locate profile with request.user.profile
  # variable for in_collection
  # use dot notation to filter through profile collection as car.id
  # tempate for my profile and collection
  # else if not logged in no collection



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

