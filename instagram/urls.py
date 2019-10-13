from django.urls import path
from .views import ImageListView,ImageDetailView,ImageCreateView
from . import views


urlpatterns = [
    path('',ImageListView.as_view(), name = 'home'),
    path('image/<int:pk>/',ImageDetailView.as_view(), name = 'image-detail'),
    path('image/new/',ImageCreateView.as_view(), name = 'image-create'),
   
]