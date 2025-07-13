from django.contrib import admin
from .models import Producto, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descuento', 'mostrar_precio_con_descuento', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('mostrar_precio_con_descuento',)

    def mostrar_precio_con_descuento(self, obj):
        return round(obj.precio_con_descuento, 2) if obj.precio_con_descuento is not None else "N/A"

    mostrar_precio_con_descuento.short_description = 'Precio con Descuento'
