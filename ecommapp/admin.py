from django.contrib import admin

from ecommapp.models import cupon, producto, categoria, cliente

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
    list_display = ('username','nombre','email','password')