from django.db import models
from artist.models import Artist
from gender.models import Gender

# Create your models here.
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

    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='reviews')