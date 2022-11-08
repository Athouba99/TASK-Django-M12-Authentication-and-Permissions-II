from multiprocessing import context
from django.shortcuts import render,redirect 
from users import forms  
from django.contrib.auth import login,authenticate,logout   
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_user(request):
    form = forms.RegistrationForm()
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("successful-signup")
            else:
                return ("error'problem with you registration'")    
    context = {"form": form, }
    return render(request, "register.html", context)  

def logout_user(request):
    logout (request) 
    return redirect ("home")

def login_user(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = login_user(request.POST)
        if form.is_valid():
            auth_user = authenticate(username = form.cleaned_data["username"],
              password = form.cleaned_data["password"])
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    context = {"form":form}
    return render (request, "longin.html", context)

@login_required
def create_movie(request):
    ...