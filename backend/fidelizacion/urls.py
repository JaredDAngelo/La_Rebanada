from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BeneficioViewSet,
    NivelViewSet,
    CuponViewSet,
    HistorialPuntosViewSet,
    HistorialBeneficioViewSet,
    PerfilClienteViewSet
)

router = DefaultRouter()
router.register(r'beneficios', BeneficioViewSet, basename='beneficio')
router.register(r'niveles', NivelViewSet, basename='nivel')
router.register(r'cupones', CuponViewSet, basename='cupon')
router.register(r'historial-puntos', HistorialPuntosViewSet, basename='historial-puntos')
router.register(r'historial-beneficios', HistorialBeneficioViewSet, basename='historial-beneficio')
router.register(r'perfiles', PerfilClienteViewSet, basename='perfil-cliente')

urlpatterns = [
    path('', include(router.urls)),
]
