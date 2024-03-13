from django.db import models
from artist.models import Artits

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    release = models.DateField()
    artits = models.ManyToManyField('Artits')
    gender = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    numberoftrack = models.IntegerField()
    track = models.CharField(max_length=50)