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

    nome_get = {
        'type': 'array', 
        'items': {
            'type': 'string' 
        }
    }    


    music_name = JSONField(schema=nome_get, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        if self.music_name:
            Music = apps.get_model('music', 'Music')
            for music_name in self.music_name:
                Music.objects.create(name=music_name, artist=self.artist, album=self)
                
    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='reviews')