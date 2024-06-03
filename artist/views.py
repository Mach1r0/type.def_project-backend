from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, pagination
from rest_framework import permissions
from .models import Artist
from .serializers import ArtistSerializer
from django.http import JsonResponse

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('-name')
    serializer_class = ArtistSerializer
    pagination_class = pagination.PageNumberPagination

    lookup_field = 'slug'
    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

def count_artist(request):
    Artist_count = Artist.objects.count()

    data = {
        'Artist_count': Artist_count,
    }
    return JsonResponse(data)