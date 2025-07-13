from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cupon, Beneficio, Nivel, PerfilCliente, HistorialBeneficio, HistorialPuntos
from .serializers import (
    CuponSerializer,
    BeneficioSerializer,
    NivelSerializer,
    PerfilClienteSerializer,
    HistorialBeneficioSerializer,
    HistorialPuntosSerializer
)
from django.utils import timezone


class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

    @action(detail=False, methods=['post'])
    def validar(self, request):
        codigo = request.data.get('codigo')
        if not codigo:
            return Response({'error': 'Código requerido'}, status=400)

        try:
            cupon = Cupon.objects.get(codigo=codigo, activo=True)
            if cupon.fecha_expiracion and cupon.fecha_expiracion < timezone.now().date():
                return Response({'error': 'Cupón expirado'}, status=400)
            return Response(CuponSerializer(cupon).data)
        except Cupon.DoesNotExist:
            return Response({'error': 'Cupón no válido'}, status=404)


class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer


class PerfilClienteViewSet(viewsets.ModelViewSet):
    queryset = PerfilCliente.objects.all()
    serializer_class = PerfilClienteSerializer

    @action(detail=True, methods=['get'])
    def beneficios(self, request, pk=None):
        perfil = self.get_object()
        beneficios = Beneficio.objects.filter(puntos_requeridos__lte=perfil.puntos)
        return Response(BeneficioSerializer(beneficios, many=True).data)


class HistorialBeneficioViewSet(viewsets.ModelViewSet):
    queryset = HistorialBeneficio.objects.all()
    serializer_class = HistorialBeneficioSerializer


class HistorialPuntosViewSet(viewsets.ModelViewSet):
    queryset = HistorialPuntos.objects.all()
    serializer_class = HistorialPuntosSerializer
