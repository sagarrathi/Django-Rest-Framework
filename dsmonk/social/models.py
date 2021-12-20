from typing_extensions import Self
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.top_name
        
class Webpage(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=264, unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    first_name=models.CharField(max_length=264)
    email_id=models.EmailField(max_length=254, unique=True, primary_key=True)

    def __str__(self):
        return str(self.first_name+"::"+self.email_id)
