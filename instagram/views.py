from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Image


def home(request):
    message = "Welcome to Instagram"

    images = Image.objects.all()
    user = User.objects.get(username=request.user.username)

    context = {
        "message":message,
        'images':images,
        'user':user
    }
    return render(request, 'instagram/home.html',context)

