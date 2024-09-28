from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError



def home(request):
    return render(request, 'home.html')
    
def signup_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
    else:
        try:
            user = User.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1'],
    
            )
            user.save()
            login(request, user)
            return redirect("home")
        except IntegrityError:
            return render(request, "signup.html", {"form": form, "error": "Username or email already exist. Try another and continue"})

def logout_user(request):
    logout(request)
    return redirect(home)