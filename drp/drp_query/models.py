from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Refugee(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=100)
    contact = models.IntegerField()
    completed = models.BooleanField(blank=False,null=False)
    attended_by = models.CharField(max_length=25)
    time_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=25)
    contact = models.IntegerField()
    alloted_to =  models.ForeignKey(Refugee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


