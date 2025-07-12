from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'nombre', 'nivel', 'puntos', 'is_staff', 'is_active']
    search_fields = ['email', 'nombre', 'telefono']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {
            'fields': ('nombre', 'telefono', 'fecha_nacimiento')
        }),
        ('Fidelización', {
            'fields': ('nivel', 'puntos')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'rol', 'groups', 'user_permissions')
        }),
        ('Fechas', {'fields': ('last_login', 'creado_en')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'nombre',
                'telefono',
                'fecha_nacimiento',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'rol',
            )
        }),
    )


admin.site.register(User, UserAdmin)
