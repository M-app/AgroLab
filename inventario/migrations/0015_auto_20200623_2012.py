# Generated by Django 2.2.12 on 2020-06-24 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_producto_presentaciones'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccionProducto',
        ),
        migrations.DeleteModel(
            name='AplicacionProducto',
        ),
        migrations.DeleteModel(
            name='CategoriaProducto',
        ),
        migrations.DeleteModel(
            name='DetalleUnitario',
        ),
        migrations.DeleteModel(
            name='Lote',
        ),
        migrations.DeleteModel(
            name='Medidas',
        ),
        migrations.DeleteModel(
            name='Presentacion',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.DeleteModel(
            name='TipoProducto',
        ),
        migrations.DeleteModel(
            name='UnidadMedidaProducto',
        ),
    ]
