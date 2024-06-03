from django.contrib.auth.models import User, Group
from rest_framework import serializers
from artist.models import Artist
from album.serializers import AlbumSerializer

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    albums = AlbumSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        depth = 1 
        fields = [
            'url',
            'name',
            'gender', 
            'location',
            'slug',
            'image',
            'albums',
        ]
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }