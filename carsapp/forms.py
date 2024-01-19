from django import forms
from .models import Car, Comment

class CarForm(forms.ModelForm):

  class Meta:
    model = Car
    fields = ('name','make','model','year','color','trim','photo_url','description',)


class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ('comment','car',)
