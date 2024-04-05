from rest_framework import serializers
from .models import Album, Review, Artist
from gender.models import Gender
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    gender = serializers.SlugRelatedField(
        many=False,  # Change this line
        queryset=Gender.objects.all(), 
        slug_field='name' 
    )
    artist = serializers.SlugRelatedField(
        many=False,
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
            'gender',
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