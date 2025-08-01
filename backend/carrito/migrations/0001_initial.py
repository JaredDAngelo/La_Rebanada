# Generated by Django 5.2.4 on 2025-07-13 00:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fidelizacion', '0001_initial'),
        ('productos', '0003_alter_producto_descuento_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('preparado', 'Preparado'), ('entregado', 'Entregado')], default='pendiente', max_length=20)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('puntos_ganados', models.PositiveIntegerField(default=0)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fidelizacion.perfilcliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='carrito.pedido')),
            ],
        ),
    ]
