from django.test import TestCase
from .models import *

# Create your tests here.
class TestImage(TestCase):

    def setUp(self):
        self.new_profile = Profile(profile_pic = 'media/default.jpg', bio = 'I love coding')
        self.new_profile.save_profile()

        self.new_image = Image(image='media/default.jpg', image_name='hacker', image_caption='This guy is a real hacker',
                               profile=self.new_profile, likes=0)
        self.new_image.save_image()


    def test_isinstance(self):
        self.new_image = Image(image='media/default.jpg', image_name='hacker', image_caption='This guy is a real hacker',
                               profile=self.new_profile, likes=0)
        self.new_image.save_image()

        self.assertTrue(isinstance(self.new_image,Image))