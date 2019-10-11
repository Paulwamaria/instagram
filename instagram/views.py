from django.shortcuts import render

def home(request):
    message = "Welcome to Instagram"

    context = {
        "message":message
    }
    return render(request, 'instagram/home.html',context)