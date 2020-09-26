from rest_framework import serializers

from ecommapp.models import producto, categoria, cupon, cliente, pedido, detalle_pedido
from ecommapp.models import estado_pedido

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
    # def validate(self, data):   #Es invocado antes de save
        # if not data['codigo']:
        #     raise serializers.ValidationError({"data": "Cupon no existe", "error": True})
        #return data
    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existe Cupon", "error": True})
    # def retrieve(self, request, *args, **kwargs):
    class Meta:
        model = cupon
        fields = '__all__'

# class ClienteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = cliente
#         fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    emailCli = serializers.EmailField
    def retrieve(self, data):
        if not data:
            raise serializers.ValidationError({"data": "No existen clientes", "error": True})
    # def validate(self, data):
    #     data["email"]  #self.initial_data["email"]
    class Meta:
        model = cliente
        fields = '__all__'
    # def create(self, data):
    #     emailCli = data["email"]
    #     queryset = cliente.objects.all()
    #     queryset = queryset.filter(email=emailCli)
    #     if queryset:
    #         raise serializers.ValidationError({"data": "Cliente ya está registrado", "error": True})
    #     else:
    #         objCliente = cliente.objects.create(**data)
    #         return objCliente
    # def save(self):
    #     raise serializers.ValidationError({"data": "Cliente se actualiza o registra", "error": False})

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