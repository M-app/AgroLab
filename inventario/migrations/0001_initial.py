# Generated by Django 2.2.12 on 2020-04-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=8)),
                ('nombre_banco', models.CharField(max_length=30)),
                ('no_cuenta', models.CharField(max_length=20)),
                ('nombre_vendedor', models.CharField(max_length=30)),
                ('telefono_vendedor', models.CharField(max_length=8)),
            ],
        ),
    ]
