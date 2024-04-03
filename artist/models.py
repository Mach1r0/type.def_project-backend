from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    GENDER_CHOICES = [
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other"),
    ]
    
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
