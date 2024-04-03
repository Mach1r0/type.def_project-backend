from rest_framework import serializers
from .models import Album, Review, Artist
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    artist = serializers.SlugRelatedField(
        many=True,
        queryset=Artist.objects.all(), 
        slug_field='name' 
     )

    class Meta: 
        model =  Album 
        depth = 1
        fields = [
            'url',
            'image',  
            'name',
            'slug',
            'release',
            'description',
            'gender',
            'artist',
            'reviews',
        ]

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.SlugRelatedField(
        many=False,
        queryset=Album.objects.all(),
        slug_field='slug'  # Use 'slug' instead of 'name'
    )

    class Meta:
        model = Review
        depth = 1
        fields = [
            'title',
            'content',
            'stars',
            'album',
        ]