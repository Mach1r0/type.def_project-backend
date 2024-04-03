from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from .models import Gender, Subgenres
from .serializers import GenderSerializers, SubGenresSerializers

class GendersViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializers

class SubgenresViewSet(viewsets.ModelViewSet):
    queryset = Subgenres.objects.all()
    serializer_class = SubGenresSerializers