from django.shortcuts import render

# Create your views here.

from .models import detalle_pedido
from .serializers import DetalleSerializer
from rest_framework import viewsets

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = detalle_pedido.objects.all()
    serializer_class = DetalleSerializer