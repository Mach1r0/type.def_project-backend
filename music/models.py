from django.db import models
from artist.models import Artist
from album.models import Album
from django_jsonform.models.fields import JSONField
from django.http import HttpResponse

class Music(models.Model):  
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=50, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics')

    def __str__(self):
        return self.name

