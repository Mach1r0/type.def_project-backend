from django.contrib.auth.models import User, Group
from rest_framework import serializers
from artist.models import Artist
from album.models import Album

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    albums = serializers.SlugRelatedField(
        many=True, 
        queryset=Album.objects.all(),
        slug_field='name'
        )
    class Meta:
        model = Artist
        fields = '__all__'