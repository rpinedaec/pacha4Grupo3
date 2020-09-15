from django.contrib import admin

from ecommapp.models import cupon

class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

admin.site.register(cupon, cuponAdmin)