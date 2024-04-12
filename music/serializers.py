from rest_framework import serializers
from .models import Music
from artist.models import Artist
from album.models import Album

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.SlugRelatedField(
        many=False, 
        queryset=Artist.objects.all(), 
        slug_field='slug'
    )  
    album = serializers.SlugRelatedField(
        many=False,
        queryset=Album.objects.all(),
        slug_field='slug'
    )

    class Meta: 
        model = Music
        depth = 1
        fields = [
            'name',
            'time',
            'artist',
            'album',  # Include 'album' in fields
        ]