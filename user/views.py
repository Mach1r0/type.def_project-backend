from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from user.models import User
from user.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
