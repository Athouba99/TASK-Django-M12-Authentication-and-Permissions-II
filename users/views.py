from django.shortcuts import render,redirect
from .forms import Registration 
from django.contrib import login  
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