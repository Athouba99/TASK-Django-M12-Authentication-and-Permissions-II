from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        field = ["username", "first_name", "last_name", "email", "password"]
        widgets = {  "password": forms.PasswordInput(),}


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    
