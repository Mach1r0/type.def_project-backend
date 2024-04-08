from rest_framework import serializers
from .models import Album, Review, Artist
from gender.models import Gender

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.SlugRelatedField(
        many=False,
        queryset=Album.objects.all(),
        slug_field='slug'
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

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    gender = serializers.SlugRelatedField(
        many=False,
        queryset=Gender.objects.all(), 
        slug_field='name' 
    )
    artist = serializers.SlugRelatedField(
        many=False,
        queryset=Artist.objects.all(), 
        slug_field='name' 
     )
    reviews = ReviewSerializer(many=True, read_only=True)

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
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }