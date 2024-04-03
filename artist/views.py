from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from .models import Artist
from .serializers import ArtistSerialaizer 

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('-name')
    serializer_class = ArtistSerialaizer
