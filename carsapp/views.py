from django.shortcuts import render, redirect
from .models import Car, Comment
from .forms import CarForm, CommentForm
# Create your views here.



def car_list(request):
  cars = Car.objects.all()
  return render(request, 'carsapp/car_list.html', {'cars':cars})

def car_detail(request,pk):
  car = Car.objects.get(id=pk)
  return render(request, 'carsapp/car_detail.html', {'car':car})

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
  
def comment_add(request):
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save()
      return redirect('comment_detail',pk=comment.pk)
  else:
      form = CommentForm()

  return render(request, 'carsapp/comment_form.html', {'form': form})

def get_car_id(request, car_id):
    car = Car.objects.get(id=car_id)
    form = CarForm(initial={'car_id': car_id})  # replace 'field' with the actual field name
    return render(request, 'carsapp/car_detail.html', {'form': form})



def add_car_comment(req, car_id):
  car = Car.objects.get(id=car_id)
  if req.method == 'POST':
    form = CommentForm(req.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.car_id = car_id
      new_comment.save()
    return redirect('car_detail', pk=car.pk)
  else:
    form = CommentForm()
    return render(req, 'carsapp/comment_form.html', {'form': form})