from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic =  models.ImageField(upload_to='media/', default='media/default.jpg')
    bio = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to='media/', default='media/default.jpg')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name


class Comment(models.Model):
    comments = models.TextField()
    image =models.ForeignKey(Image, on_delete = models.CASCADE)