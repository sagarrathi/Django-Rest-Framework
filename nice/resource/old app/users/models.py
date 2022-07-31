from django.db import models
# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default="default.png", upload_to='profile_pics')
    slug=models.SlugField()
    bio=models.CharField(max_length=200, blank=True)
    friends=models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/user/"+str(self.slug)

def pos