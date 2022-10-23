from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import Registration 
from .forms import Login 
from django.contrib.auth import logout 
from django.contrib.auth import login,authenticate   
# Create your views here.

def register_user(request):
    form = Registration()

    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("successful-signup")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)  

def logout_user(request):
    logout (request) 
    return redirect ("success-page")

def login_user(request):
    form = Login()
    if request.method == "POST":
        form = login_user(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("successful-longin")
    context = {"form":form, }
    return render (request, "longin.html", context)