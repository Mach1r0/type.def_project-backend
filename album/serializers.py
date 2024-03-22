from django.contrib.auth.models import User, Group
from rest_framework import serializers
from album.models import Album, Review

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model =  Album 
        depth = 1
        fields = [
                'url',
                'name',
                'slug',
                'release',
                'description',
                'gender',
                'artits',
                'reviews',
                ]

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        depth = 1
        fields = [
                'title',
                'content',
                'stars',
                'album',
                ]