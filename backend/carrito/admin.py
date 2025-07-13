from django.contrib import admin
from .models import Pedido, ItemPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente', 'estado', 'total', 'puntos_ganados', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('perfil__user__correo',)
    readonly_fields = ('total', 'puntos_ganados', 'fecha_creacion')
    ordering = ('-fecha_creacion',)

    def get_cliente(self, obj):
        return obj.perfil.user.nombre  # o .correo si prefieres
    get_cliente.short_description = 'Cliente'


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario', 'get_subtotal')
    search_fields = ('producto__nombre',)
    readonly_fields = ('precio_unitario', 'get_subtotal')

    def get_subtotal(self, obj):
        return obj.subtotal()
    get_subtotal.short_description = 'Subtotal'
