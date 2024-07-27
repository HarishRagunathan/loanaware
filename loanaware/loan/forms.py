from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Age'}))
    annual_income=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Annual income'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your confrim password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2','age','annual_income']