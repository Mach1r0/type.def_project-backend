from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from .models import Artist
from .serializers import ArtistSerializer
from django.http import JsonResponse

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('-name')
    serializer_class = ArtistSerializer

def count_artist(request):
    Artist_count = Artist.objects.count()

    data = {
        'Artist_count': Artist_count,
    }
    return JsonResponse(data)