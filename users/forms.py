from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model 
from django.db import models
from pkg_resources import require


user = get_user_model()

class Registration(forms.ModelForm):
    class Meta:
        model = user
        field = ["username", "first_name", "last_name", "email", "password"]
        widgets = {  "password": forms.PasswordInput(),
        }


class Login(forms.Form):
    username = models.CharField(required=True)
    password = models.CharField(required=True, widget=forms.PasswordInput())
    
