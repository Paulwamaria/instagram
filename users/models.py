from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =  models.ImageField(upload_to='media/', default='media/default.jpg')
    bio = models.TextField()


    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)

            img.thumbnail(output_size)
            img.save(self.profile_pic.path)