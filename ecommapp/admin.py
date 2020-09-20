from django.contrib import admin

from ecommapp.models import cupon, producto, categoria, pedido, detalle_pedido, cliente
from ecommapp.models import estado_pedido

class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

admin.site.register(cupon, cuponAdmin)

class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria','igv','imagen','precio', 'descuento' )

admin.site.register(producto, productoAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion' )

admin.site.register(categoria, categoriaAdmin)

class clienteAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'email', 'password' )

admin.site.register(cliente, clienteAdmin)

class pedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'subtotal', 'igv', 'total', 'cliente', 'estado', 'cupon' )

admin.site.register(pedido, pedidoAdmin)

class detallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'subtotal' )

admin.site.register(detalle_pedido, detallePedidoAdmin)

class estadoPedidoAdmin(admin.ModelAdmin):
    field = ('descripcion' )

admin.site.register(estado_pedido, estadoPedidoAdmin)