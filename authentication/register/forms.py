from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm #built in form
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #Ana UserCreationFormunu değiştirmek için Meta ismi önemli
        model = User
        fields = ["username", "email", "password1", "password2"]
