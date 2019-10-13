from django.shortcuts import render,redirect, get_object_or_404
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

def like(request, image_id):
    image = get_object_or_404(Image, pk=image_id)


class UserImageListView(ListView):
    model = Image
    template_name='instagram/home.html'
    context_object_name ='images'
    ordering = ['-created_on']


    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Image.objects.filter(profile=user.profile).order_by('-created_on')



def search_results(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        searched_users = User.objects.filter(username__icontains=search_term)
        message=search_term
        return render(request, "instagram/user_image.html", {"images":searched_users, "message":message})

    else:
        message = "Search term not found"

        return render(request,'instagram/search.html',{"message":message})