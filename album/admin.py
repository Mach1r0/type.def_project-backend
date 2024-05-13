from django.contrib import admin 
from album.models import Album

class ListaAlbum(admin.ModelAdmin):
    list_display = ("name", 'id', 'type')
    search_fields = ("id", 'nome')
    list_per_page = 10

admin.site.register(Album, ListaAlbum)

