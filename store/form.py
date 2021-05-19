# import form class from django 
from django import forms 
from django.db import models
from .models import ShippingAddress
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
  
# create a ModelForm 
class ShippingForm(forms.ModelForm): 
    # specify the name of model to use
    name=models.CharField (max_length=50)
    class Meta: 
        model = ShippingAddress
        fields = "__all__"
        widgets = {'customer': forms.HiddenInput(),'order': forms.HiddenInput()}
