from rest_framework import viewsets 
from rest_framework import permissions
from user.models import User  # Import User from models.py
from rest_framework.response import Response
from rest_framework import status 
from user.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RegisterUserSerializer
import hashlib
from django.shortcuts import get_object_or_404

# Define a custom viewset for user registration
class UserView(viewsets.ViewSet):
    def create(self, request):
        user_serializer = RegisterUserSerializer(data=request.data)
        test_user = request.data.get('email', None)
        
        try:
            User.objects.get(email=test_user)
            return Response({"error": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            if user_serializer.is_valid():
                user = user_serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)  # Pass the user instance
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            delete_user = User.objects.get(pk=pk)
            delete_user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        name = request.data.get('name')
        try:
            update_user = User.objects.get('name')
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
