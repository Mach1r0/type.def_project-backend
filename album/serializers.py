from django.contrib.auth.models import User, Group
from rest_framework import serializers
from album.models import Album

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model =  Album 
        fields = '__all__'
