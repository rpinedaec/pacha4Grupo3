"""ecommprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommapp.views import ProductoViewSet, CategoriaViewSet, CuponViewSet, PedidoViewSet
from ecommapp.views import ClienteViewSet, detallePedidoViewSet, estadoPedidoViewSet, payCulqi
from ecommapp.views import getPedido, loginCliente
from django.conf.urls import url

router = routers.DefaultRouter()

router.register(r'producto', ProductoViewSet, basename = 'producto')
router.register(r'categoria', CategoriaViewSet, basename = 'categoria')
router.register(r'cupon', CuponViewSet, basename = 'cupon')
router.register(r'cliente', ClienteViewSet, basename = 'cliente')
router.register(r'estado_pedido', estadoPedidoViewSet, basename = 'estado_pedido')
router.register(r'pedido', PedidoViewSet, basename = 'pedido')
router.register(r'detalle_pedido', detallePedidoViewSet, basename = 'detalle_pedido')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'getPedido', getPedido),
    url(r'loginCliente', loginCliente),
    url(r'payCulqi', payCulqi)
]
