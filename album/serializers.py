from django.contrib.auth.models import User, Group
from rest_framework import serializers
from album.models import Album, Review

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model =  Album 
        fields = '__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'