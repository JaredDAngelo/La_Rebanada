from rest_framework import serializers
from .models import Pedido, ItemPedido
from productos.models import Producto
from productos.serializers import ProductoSerializer

class ItemPedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), write_only=True, source='producto'
    )
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemPedido
        fields = ['id', 'producto', 'producto_id', 'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['subtotal', 'precio_unitario']

    def get_subtotal(self, obj):
        return obj.cantidad * obj.precio_unitario


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    puntos_ganados = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'perfil', 'estado', 'fecha_creacion', 'total', 'puntos_ganados', 'items']
        read_only_fields = ['total', 'puntos_ganados', 'fecha_creacion']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            producto = item_data['producto']
            cantidad = item_data['cantidad']
            # Usa el precio con descuento si existe
            precio_unitario = producto.precio_con_descuento() if callable(producto.precio_con_descuento) else producto.precio
            subtotal = cantidad * precio_unitario
            total += subtotal

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )

        pedido.total = total
        pedido.puntos_ganados = int(total // 1000)  # 1 punto por cada 1000
        pedido.save()

        # Actualizar perfil del cliente
        perfil = pedido.perfil
        perfil.puntos += pedido.puntos_ganados
        perfil.pedidos_realizados += 1
        perfil.save()

        return pedido
