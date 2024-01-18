from django.shortcuts import render

# Create your views here.

from .models import Car, Comment

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
      return redirect('car_detail,pk=car.pk')
    else:
      form = CarForm()

    return render(request, 'car_form.html', {'form': form})
  
  def comment_add(request):
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save()
      return redirect('comment_detail,pk=comment.pk')
    else:
      form = CommentForm()

    return render(request, 'comment_form.html', {'form': form})