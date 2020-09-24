from rest_framework import serializers

from ecommapp.models import *

class ProductoSerializer(serializers.ModelSerializer):

    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existe Curso", "error": True})
    class Meta:
        model = producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    
    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existen categorias", "error": True})
    class Meta:
        model = categoria
        fields = '__all__'

class CuponSerializer(serializers.ModelSerializer):

    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existe Cupon", "error": True})

    class Meta:
        model = cupon
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    
    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existen Pedidos", "error": True})
    class Meta:
        model = pedido
        fields = '__all__'

class detallePedidoSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if not data["pedido"]:
            raise serializers.ValidationError({"data": "Se requiere # de Pedido para detalle", "error": True})
        return data
    class Meta:
        model = detalle_pedido
        fields = '__all__'

class estadoPedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = estado_pedido
        fields = '__all__'