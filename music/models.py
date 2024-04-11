from django.db import models
from artist.models import Artist

class Musica(models.Models):
    nome = models.CharField(max_length=255)
    time = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')    

    def __str__(self):
        return self.name
    