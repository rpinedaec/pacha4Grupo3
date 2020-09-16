from rest_framework import serializers
from .models import detalle_pedido

class DetalleSerializer(serializers.Serializer):

    class Meta:
        model = detalle_pedido
        fields = '__all__'
