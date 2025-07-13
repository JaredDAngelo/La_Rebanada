from django.db import models
from django.utils import timezone
from productos.models import Producto
from fidelizacion.models import PerfilCliente

ESTADOS_PEDIDO = (
    ('pendiente', 'Pendiente'),
    ('preparado', 'Preparado'),
    ('entregado', 'Entregado'),
)

class Pedido(models.Model):
    perfil = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    puntos_ganados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.perfil.user.nombre}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"
