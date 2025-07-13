from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, ItemPedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'items', ItemPedidoViewSet, basename='item-pedido')

urlpatterns = [
    path('', include(router.urls)),
]
