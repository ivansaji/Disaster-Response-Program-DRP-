from django.db import models
from django.utils import timezone

# Create your models here.

class Refugee(models.Model):
    name = models.CharField(max_length = 25)
    contact = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now_add=True)
    location = models.TextField()
    threat_rating = models.IntegerField()
    necessities = models.TextField()
    no_of_people = models.IntegerField()

class Volunteer(models.Model):
    name = models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now_add=True)