from django.db import models
from artist.models import Artist
from gender.models import Gender
from django_jsonform.models.fields import JSONField
from django.apps import apps

class Album(models.Model):
    TYPE_CHOICE = [
        ('ep', 'EP'),
        ('album', 'Album'),
    ]
   
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='albums/', null=True, blank=True)
    slug = models.CharField(max_length=100, unique=True, blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICE, max_length=30)
    release = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')    
    description = models.CharField(max_length=400)
    genders = models.ManyToManyField(Gender, related_name='albums')

    music_info_schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'time': {'type': 'string'}  
            },
            'required': ['name', 'time']
        }
    }
    music_info = JSONField(schema=music_info_schema, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        if self.music_info:
            Music = apps.get_model('music', 'Music')
            for music_info_item in self.music_info:
                Music.objects.create(name=music_info_item['name'], time=music_info_item['time'], artist=self.artist, album=self)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='reviews')