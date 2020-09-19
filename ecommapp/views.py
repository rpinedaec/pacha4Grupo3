#from django.shortcuts import render
from rest_framework import viewsets
from ecommapp.serializers import ProductoSerializer, CategoriaSerializer, CuponSerializer
from ecommapp.serializers import PedidoSerializer, ClienteSerializer
from ecommapp.models import producto, categoria, cupon, cliente, pedido
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class ProductoViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductoSerializer
#     #permission_classes = [IsAuthenticated,]
#     queryset = producto.objects.all()
#     serializer_class = ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = producto.objects.all()
        prodNom = self.request.query_params.get('nombre',None)
        prodId = self.request.query_params.get('id',None)
        if prodNom is not None:
            queryset = queryset.filter(nombre=prodNom)
        if prodId is not None:
            queryset = queryset.filter(id=prodId)
        return queryset
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    #queryset = categoria.objects.all()
    queryset = categoria.objects.filter()
    serializer_class = CategoriaSerializer

# class CuponViewSet(viewsets.ModelViewSet):
#     queryset = cupon.objects.filter()
#     serializer_class = CuponSerializer

class CuponViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = cupon.objects.filter()
        cupCod = self.request.query_params.get('codigo',None)
        if cupCod is not None:
            queryset = queryset.filter(codigo=cupCod)
        return queryset
    serializer_class = CuponSerializer

# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset = cliente.objects.filter()
#     serializer_class = ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = cliente.objects.filter()
        cliUname = self.request.query_params.get('username',None)
        cliPass = self.request.query_params.get('password',None)
        # cliId = self.request.query_params.get('id',None)
        if cliUname is not None:
            queryset = queryset.filter(username=cliUname, password=cliPass)
        # if cliId is not None:
        #     queryset = queryset.filter(id=cliId)
        return queryset
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer
