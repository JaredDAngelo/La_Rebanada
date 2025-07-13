from rest_framework import serializers
from .models import Cupon, Beneficio, Nivel, PerfilCliente, HistorialBeneficio, HistorialPuntos
from users.models import User


class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = '__all__'


class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficio
        fields = '__all__'


class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'


class PerfilClienteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PerfilCliente
        fields = '__all__'


class HistorialBeneficioSerializer(serializers.ModelSerializer):
    beneficio = BeneficioSerializer(read_only=True)

    class Meta:
        model = HistorialBeneficio
        fields = '__all__'


class HistorialPuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPuntos
        fields = '__all__'
