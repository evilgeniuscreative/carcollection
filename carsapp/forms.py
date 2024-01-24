from django import forms
from .models import Car, Comment, User, Profile


class UserCreationForm(forms.ModelForm):
  
    class Meta:
      model = User
      fields = ('username','password',)


class AuthenticationForm(forms.ModelForm):
  
    class Meta:
      model = User
      fields = ('username','password',)


class CarForm(forms.ModelForm):

  class Meta:
    model = Car
    fields = ('name','make','model','year','color','trim','photo_url','description',)


class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ('comment',)


# class AddToCollectionForm(forms.ModelForm):

#   class Meta:
#     model = Favorite
#     fields = ('car','user',)