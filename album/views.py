from rest_framework import viewsets 
from rest_framework import permissions
from album.models import Album
from album.serializers import AlbumSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-name')
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
