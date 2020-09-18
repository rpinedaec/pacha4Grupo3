from rest_framework import serializers

from ecommapp.models import producto, categoria
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

# class ProductodetalleSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = producto
#         fields = '__all__'      