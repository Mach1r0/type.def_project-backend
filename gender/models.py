from django.db import models

# Create your models here.
class Gender(models.Model):
    imagem = models.ImageField(upload_to='generos/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subgenres(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name