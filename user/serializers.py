from django.contrib.auth.models import User, Group
from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )     
        return user
    
    class Meta:
        model = User  # Assign User to the model attribute
        fields = [
            'url',
            'email',
            'name',
            'password'
        ]