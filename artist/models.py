from django.db import models
from django.utils.text import slugify

class Artist(models.Model):
    GENDER_CHOICES = [
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other"),
    ]
    
    name = models.CharField(max_length=50) 
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10) 
    location = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, unique=True, blank=True) 
    image = models.ImageField(upload_to='artists/', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name