from django.contrib.auth.models import User, Group
from ecommapp.models import cupon, estado_pedido, categoria, cliente, producto, pedido, detalle_pedido
from rest_framework import serializers

class CuponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cupon
        fields = '__all__'

class Estado_PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estado_pedido
        fields = '__all__'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'
class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'

class Detalle_PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = detalle_pedido
        fields = '__all__'
