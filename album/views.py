from rest_framework import viewsets 
from django.shortcuts import render
from rest_framework import permissions
from album.models import Album, Review
from album.serializers import AlbumSerializer, ReviewSerializer
from django.http import JsonResponse

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-name')
    serializer_class = AlbumSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by()
    serializer_class = ReviewSerializer

def count_view(request):
    Album_count = Album.objects.count()
    Review_count = Review.objects.count()

    data = {
        'Album_count': Album_count,
        'Review_count': Review_count,
    }
    return JsonResponse(data)