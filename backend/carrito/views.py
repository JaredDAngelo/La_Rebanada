from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Pedido, ItemPedido
from .serializers import PedidoSerializer, ItemPedidoSerializer
from fidelizacion.models import PerfilCliente

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().select_related('perfil').prefetch_related('items')
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfilcliente'):
            return Pedido.objects.filter(perfil=user.perfilcliente)
        return super().get_queryset()

    def perform_create(self, serializer):
        perfil = PerfilCliente.objects.get(user=self.request.user)
        pedido = serializer.save(perfil=perfil)

        # Calcular total del pedido y puntos ganados
        total = 0
        for item in pedido.items.all():
            subtotal = item.cantidad * item.precio_unitario
            total += subtotal

        puntos = int(total // 1000)  # ejemplo: 1 punto cada $1000

        pedido.total = total
        pedido.puntos_ganados = puntos
        pedido.save()

        # Actualizar perfil del cliente
        perfil.puntos += puntos
        perfil.pedidos_realizados += 1
        perfil.save()

    @action(detail=False, methods=['get'])
    def mis_pedidos(self, request):
        user = request.user
        if not hasattr(user, 'perfilcliente'):
            return Response({'error': 'El usuario no tiene perfil asociado'}, status=status.HTTP_400_BAD_REQUEST)
        pedidos = Pedido.objects.filter(perfil=user.perfilcliente)
        serializer = self.get_serializer(pedidos, many=True)
        return Response(serializer.data)


class ItemPedidoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemPedido.objects.all().select_related('pedido', 'producto')
    serializer_class = ItemPedidoSerializer
    permission_classes = [IsAuthenticated]
