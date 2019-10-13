from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Image
from users.models import Profile


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

class ImageListView(ListView):
    model = Image
    template_name='instagram/home.html'
    context_object_name ='images'
    ordering = ['-created_on']

class ImageDetailView(DetailView):
    model = Image

class ImageCreateView(LoginRequiredMixin,CreateView):
     
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

class ImageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


    def test_func(self):
        image = self.get_object()

        if self.request.user == image.profile:
            return True

        return False

class ImageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Image
    success_url = ('/')
    def test_func(self):
        image = self.get_object()

        if self.request.user.profile == image.profile:
            return True

        return False