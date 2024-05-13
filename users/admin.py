from django.contrib import admin
from .models import User

@admin.register(User)
class ListUsers(admin.ModelAdmin):
        list_display = ('name', 'email', 'is_active', 'is_staff', 'is_superuser')
        search_fields = ('name', 'email')
        list_per_page =10 
    

    