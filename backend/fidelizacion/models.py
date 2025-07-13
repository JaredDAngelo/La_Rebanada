from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cupon(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    tipo_descuento = models.CharField(
        max_length=10,
        choices=(('porcentaje', 'Porcentaje'), ('valor', 'Valor fijo'))
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    usos_maximos = models.PositiveIntegerField(default=1)
    usos_actuales = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_expiracion = models.DateField()

    def __str__(self):
        return self.codigo

    def es_valido(self):
        return self.activo and self.usos_actuales < self.usos_maximos


class Beneficio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    puntos_requeridos = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    nombre = models.CharField(max_length=50)
    puntos_minimos = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.PositiveIntegerField(default=0)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True, blank=True)
    pedidos_realizados = models.PositiveIntegerField(default=0)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.nombre}"


class HistorialBeneficio(models.Model):
    perfil = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE)
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.perfil.user.nombre} - {self.beneficio.nombre}"


class HistorialPuntos(models.Model):
    perfil = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, related_name='movimientos_puntos')
    fecha = models.DateTimeField(auto_now_add=True)
    puntos = models.IntegerField()
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.perfil.user.nombre} - {self.puntos} pts - {self.motivo}"
