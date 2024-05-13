from django.db import models
from artist.models import Artist
from album.models import Album
from django_jsonform.models.fields import JSONField
from django.http import HttpResponse

class Music(models.Model):  
    name = models.CharField(max_length=255)
    time = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics')

    def __str__(self):
        return self.name
    
    ALBUMS_ITEMS = {
        'type': 'array', 
        'items': {
            'type': 'object',
            'properties': {
                'album': {
                    'type': 'string'
                }
            }
        }
    }

    album_info = JSONField(schema=ALBUMS_ITEMS)
