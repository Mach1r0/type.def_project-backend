from rest_restwork import serializers 
from .models import Gender, subgenres 

class GenderSerializers(serializers.HyperlinkedModelSerializer):
    imagem = serializers.ImageField(max_length=None, use_url=True)
    class Meta: 
        model = Gender
        fields = [
            nome, 
        ]
