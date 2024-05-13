from django.contrib import admin 
from album.models import Album, Review

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'release', 'artist']
    search_fields = ['name', 'artist__name']
    list_filter = ['type', 'release', 'artist']
    filter_horizontal = ['genders']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'stars', 'album']
    search_fields = ['title', 'album__name']
    list_filter = ['stars', 'album']