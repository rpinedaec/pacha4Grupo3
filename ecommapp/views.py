#from django.shortcuts import render
from rest_framework import viewsets
from ecommapp.serializers import ProductoSerializer
from ecommapp.models import producto
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer    
