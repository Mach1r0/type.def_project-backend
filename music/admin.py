from django.contrib import admin 
from music.models import Music

class ListaMusic(admin.ModelAdmin):
    list_display = ("name", 'id')
    search_fields = ("id", 'nome')
    list_per_page = 10

admin.site.register(Music, ListaMusic)

