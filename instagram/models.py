from django.db import models

from django.contrib.auth.models import User
from users.models import Profile
    

class Image(models.Model):
    image = models.ImageField(upload_to='media/', default='media/default.jpg')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Comment(models.Model):
    content = models.TextField()
    image =models.ForeignKey(Image, on_delete = models.CASCADE)

    def __str__(self):
        return self.content

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()