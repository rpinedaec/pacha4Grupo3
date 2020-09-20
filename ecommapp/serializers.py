from rest_framework import serializers

from ecommapp.models import producto, categoria, cupon, cliente, pedido, detalle_pedido
from ecommapp.models import estado_pedido
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

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'

class detallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalle_pedido
        fields = '__all__'

class estadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estado_pedido
        fields = '__all__'