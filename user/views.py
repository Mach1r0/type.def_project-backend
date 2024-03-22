from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import permissions
from user.models import User
from rest_framework.response import Response
from rest_framework import status 
from user.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
import hashlib

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserView(viewsets.ViewSet):
    def create(self, request):
        user_serializer = UserSerializer(data=request.data)
        test_user = request.data.get('email', None)
        
        try:
            User.objects.get(email=test_user)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            if user_serializer.is_valid():
                user = user_serializer.save()
                # Django's built-in password hashing mechanism
                user.set_password(request.data.get('password', None))
                user.save()

                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
