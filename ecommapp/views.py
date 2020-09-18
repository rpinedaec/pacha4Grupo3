#from django.shortcuts import render
from rest_framework import viewsets
from ecommapp.serializers import ProductoSerializer, CategoriaSerializer 
#ProductodetalleSerializer
from ecommapp.models import producto, categoria
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    #permission_classes = [IsAuthenticated,]
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    #queryset = categoria.objects.all()
    queryset = categoria.objects.filter()
    serializer_class = CategoriaSerializer

# class ProductodetalleViewSet(viewsets.ModelViewSet):
#     #serializer_class = ProductoSerializer
#     #permission_classes = [IsAuthenticated,]
#     def get_queryset(self):
#         queryset = producto.objects.all()
#         #desc = self.request.query_params.get('id',None)
#         desc = self.request.query_params.get('id')
#         if desc is not None:
#             queryset = queryset.filter(id=desc)
#         return queryset
#     # queryset = producto.objects.filter(nombre=lsNombre)
#     serializer_class = ProductodetalleSerializer        
