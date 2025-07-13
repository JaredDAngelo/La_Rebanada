from django.contrib import admin
from .models import Beneficio, Nivel, Cupon, PerfilCliente, HistorialBeneficio


@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'puntos_requeridos')
    search_fields = ('nombre',)
    ordering = ('puntos_requeridos',)


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'puntos_minimos')
    search_fields = ('nombre',)
    ordering = ('puntos_minimos',)


@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo_descuento', 'valor', 'activo', 'usos_actuales', 'usos_maximos', 'fecha_expiracion')
    list_filter = ('activo', 'tipo_descuento')
    search_fields = ('codigo',)
    ordering = ('-fecha_expiracion',)


@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'nivel', 'puntos', 'pedidos_realizados', 'fecha_nacimiento')
    search_fields = ('user__username', 'user__email')
    list_select_related = ('user', 'nivel')


@admin.register(HistorialBeneficio)
class HistorialBeneficioAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'beneficio', 'fecha')
    list_select_related = ('perfil', 'beneficio')
    ordering = ('-fecha',)
