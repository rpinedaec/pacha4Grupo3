#from django.shortcuts import render
from rest_framework import viewsets
from ecommapp.serializers import ProductoSerializer, CategoriaSerializer, CuponSerializer
from ecommapp.serializers import PedidoSerializer, ClienteSerializer, detallePedidoSerializer, estadoPedidoSerializer
from ecommapp.models import producto, categoria, cupon, cliente, pedido, detalle_pedido, estado_pedido
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

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

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.filter()
    serializer_class = ClienteSerializer

# class ClienteViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         queryset = cliente.objects.filter()
#         cliUname = self.request.query_params.get('username',None)
#         cliPass = self.request.query_params.get('password',None)
#         if cliUname is not None:
#             queryset = queryset.filter(username=cliUname, password=cliPass)
#         return queryset
#     serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = pedido.objects.all()
        clieId = self.request.query_params.get('cliente',None)
        if clieId is not None:
            queryset = queryset.filter(cliente=clieId)
        return queryset
    serializer_class = PedidoSerializer

class detallePedidoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = detalle_pedido.objects.all()
        pedId = self.request.query_params.get('pedido',None)
        if pedId is not None:
            queryset = queryset.filter(pedido=pedId)
        return queryset
    serializer_class = detallePedidoSerializer

class estadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = estado_pedido.objects.all()
    serializer_class = estadoPedidoSerializer

@csrf_exempt
def getPedido(request):
    queryset = pedido.objects.all().values()
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body)
            idPedido = int(jsonData["idPedido"])
            queryset = queryset.filter(id=idPedido)

            if queryset:
                querysetDet = detalle_pedido.objects.all().values()
                querysetDet = querysetDet.filter(pedido=idPedido)
            else:
                return JsonResponse({"data": "Pedido no existe", "error": True})
        except Exception as e:
            return JsonResponse({"data": e, "error": True})

    #return JsonResponse({"mensaje": "ok"})
    return JsonResponse({"pedido": list(queryset), "detalle": list(querysetDet), "error": False})

@csrf_exempt
def loginCliente(request):
    queryset = cliente.objects.all().values()
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body)
            cliUname = str(jsonData["username"])
            cliPass = str(jsonData["password"])
            if cliUname is not None:
                queryset = queryset.filter(username=cliUname, password=cliPass)
                if not queryset:
                    return JsonResponse({"data": "Credenciales incorrectas", "error": True})
        except Exception as e:
            return JsonResponse({"data": e, "error": True})

    return JsonResponse({"cliente": list(queryset), "error": False})