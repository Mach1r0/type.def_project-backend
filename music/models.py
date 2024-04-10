from django.db import models

# Create your models here.
class Musica(models.Models):
    nome = models.CharField(max_length=255)
    time = models.FloatField()
    