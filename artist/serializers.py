from django.contrib.auth.models import User, Group
from rest_framework import serializers
from artist.models import Artist

class ArtistSerialaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

        