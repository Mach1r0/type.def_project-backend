from rest_framework import viewsets, pagination
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from album.models import Album, Review
from album.serializers import AlbumSerializer, ReviewSerializer
from django.http import JsonResponse
from rest_framework.response import Response

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-name')
    serializer_class = AlbumSerializer
    pagination_class = pagination.PageNumberPagination

    lookup_field = 'slug'
    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj
    
    def get_queryset(self):
        return Album.objects.all()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by()
    serializer_class = ReviewSerializer
    pagination_class = pagination.PageNumberPagination  # Add this line

def count_view(request):
    Album_count = Album.objects.count()
    Review_count = Review.objects.count()

    data = {
        'Album_count': Album_count,
        'Review_count': Review_count,
    }
    return JsonResponse(data)