from django.shortcuts import render,redirect


def home(request):
    message = "Welcome to Instagram"

    context = {
        "message":message
    }
    return render(request, 'instagram/home.html',context)

