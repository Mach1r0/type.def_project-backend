from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        passoword = validated_data.pop('password', None)
        instace = self.Meta.model(**validated_data)

        if passoword is not None:
            instace.set_password(passoword)

        instace.save()

        return instace