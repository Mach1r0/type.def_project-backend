from django.contrib import admin 
from artist.models import Artist

class ListaArtist(admin.ModelAdmin):
    list_display = ("name", 'id', 'gender', 'location', 'slug', 'image')
    search_fields = ("id", 'nome')
    list_per_page = 10

admin.site.register(Artist, ListaArtist)

