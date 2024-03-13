from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from artist.models import Artist
from artist.serializers import ArtistSerialaizer
from django_filters.rest_framework import DjangoFilterBackend

