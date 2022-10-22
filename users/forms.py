from dataclasses import field
from django import forms
from django.contrib.auth import get_user_model 
from django.db import models


user = get_user_model()

class Registration(forms.ModelForm):
    class Meta:
        model = user
        field = ["username", "first_name", "last_name", "email", "password"]
        widgets = {  "password": forms.PasswordInput(),
        }
        