from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework import serializers
from .models import Gender, Subgenres 

class GenderSerializers(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta: 
        model = Gender
        depth = 1
        fields = [
            'name', 
            'description', 
            'slug',
            'image',
        ]

class SubGenresSerializers(serializers.HyperlinkedModelSerializer):
    gender = serializers.SlugRelatedField(
        many=False,
        queryset = Gender.objects.all(),
        slug_field='slug'
    )
    class Meta: 
        model = Subgenres  
        depth = 1 
        fields = [
            'name', 
            'description',
            'gender'  # Added here
        ]        
