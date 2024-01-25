from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, user_logged_in, user_logged_out, user_login_failed
from .models import Car, Comment, Profile
from .forms import CarForm, CommentForm, AddCarToCollectionForm
# Create your views here.

#LOGIN / AUTH

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # location = request.POST['location']
        # photo_url = request.POST['photo_url']
        # about = request.POST['about']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('car_list')
    form = AuthenticationForm()
    return render(request, 'carsapp/registration/signin.html', {'form':form, 'title':'log in'})


def signout(request):
   logout(request)
   return redirect('car_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            message = messages.success(request, f'account created for {username} !!')
            return redirect('/signin/', {'message':message})
    else:
        form = UserCreationForm()
    return render(request, 'carsapp/registration/signup.html', {'form': form})


# CAR CRUD

@login_required
def car_add(request):
  if request.method == "POST":
    form = CarForm(request.POST)
    if form.is_valid():
      car = form.save(commit=False)
      car.user = request.user
      car = form.save()
      return redirect('car_detail',pk=car.pk)
  else:
      form = CarForm()

  return render(request, 'carsapp/car_form.html', {'form': form})

def car_list(request):
  cars = Car.objects.all()
  return render(request, 'carsapp/car_list.html', {'cars':cars})

def car_detail(request, pk):
  car = Car.objects.get(id=pk)
  comments = Comment.objects.filter(car=car)
  form = CommentForm()
  return render(request, 'carsapp/car_detail.html', {'car': car, 'comments': comments, 'form': form})

@login_required
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

@login_required
def car_delete(_, pk):
    car = Car.objects.get(id=pk)
    car.delete()
    return redirect('car_list')


# COLLECTION

@login_required
def add_to_collection(request, pk):
  car = Car.objects.get(id=pk)
  profile = request.user.profile
  # profile.collection.add(car)
  # return redirect('car_detail', pk=car.pk)
  # car =  Car.objects.get(id=pk)
  if request.method == 'POST':
    form = AddCarToCollectionForm(request.POST, instance=car)
    if form.is_valid():
      car = form.save()
      return redirect('car_detail', pk=car.pk)
  else:
    form = AddCarToCollectionForm(instance=car)

  return render(request, 'carsapp/my_collection_add.html', {'form': form})





@login_required
def list_my_collection(request):
  profile = request.user.profile
  cars = profile.collection.all()
  return render(request, 'carsapp/my_collection_list.html', {'cars':cars})



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
   

# TODO: Edit comment, delete comment





def comment_list(request):
  comments = Comment.objects.all()
  return render(request, 'carsapp/comments_list.html',{'comments':comments})


