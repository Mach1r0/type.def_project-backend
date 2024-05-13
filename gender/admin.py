from django.contrib import admin 
from gender.models import Gender

class ListaGender(admin.ModelAdmin):
    list_display = ("name", 'id')
    search_fields = ("id", 'nome')
    list_per_page = 10

admin.site.register(Gender, ListaGender)

