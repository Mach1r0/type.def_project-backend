from django.contrib import admin 
from music.models import Music

@admin.register(Music)
class ListaMusic(admin.ModelAdmin):
    list_display = ("name", 'id')
    search_fields = ("id", 'nome')
    list_per_page = 10

