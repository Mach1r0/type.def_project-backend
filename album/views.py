from rest_framework import viewsets 
from rest_framework import permissions
from album.models import Album, Review
from album.serializers import AlbumSerializer, ReviewSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-name')
    serializer_class = AlbumSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by()
    serializer_class = ReviewSerializer

