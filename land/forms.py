from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]




class PostPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["name", "description", "image", "price"]