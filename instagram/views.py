from django.shortcuts import render,redirect
from .forms import InstaRegistrationForm

def home(request):
    message = "Welcome to Instagram"

    context = {
        "message":message
    }
    return render(request, 'instagram/home.html',context)

