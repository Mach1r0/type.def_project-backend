from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from artist.models import Artist
from artist.serializers import ArtistSerialaizer 

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('-name')
    serializer_class = ArtistSerialaizer
