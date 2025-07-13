from rest_framework import serializers
from .models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    precio_con_descuento = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    def get_precio_con_descuento(self, obj):
        return obj.precio_con_descuento()
