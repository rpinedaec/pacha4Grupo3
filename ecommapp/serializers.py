from rest_framework import serializers

from ecommapp.models import producto, categoria, cupon, cliente
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = cupon
        fields = '__all__'

# class ProductodetalleSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = producto
#         fields = '__all__'   
#   
class ClienteSerializer(serializers.Serializer):

    class Meta:
        model = cliente
        fields = '__all__'
        #list_display = ('username','nombre','email','password') 