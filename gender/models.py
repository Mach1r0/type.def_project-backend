from django.db import models
from django.utils.text import slugify

class Gender(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='genders/', null=True, blank=True)
    slug = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
            
class Subgenres(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name