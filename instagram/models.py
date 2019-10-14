from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from users.models import Profile
    

class Image(models.Model):
    image = models.ImageField(upload_to='media/uploads/', default='media/default.jpg')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank = True, related_name ='image_likes')
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('image-detail',kwargs = {'pk':self.pk} )

    


class Comment(models.Model):
    content = models.TextField()
    image =models.ForeignKey(Image, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()