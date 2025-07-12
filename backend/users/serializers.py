from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer básico para mostrar datos del usuario (no incluye la contraseña).
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_staff', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer para registrar un nuevo usuario.
    Valida la contraseña y la guarda correctamente encriptada.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label='Confirmar contraseña'
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Las contraseñas no coinciden.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # quitamos el password2 ya que no está en el modelo
        user = User.objects.create_user(**validated_data)
        return user
