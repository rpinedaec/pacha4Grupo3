from django.contrib import admin

from ecommapp.models import cupon, producto, categoria, pedido, detalle_pedido, cliente

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