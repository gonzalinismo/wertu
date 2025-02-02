# Generated by Django 2.1.7 on 2019-05-24 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoriaTienda', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombreCategoriaTienda', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigoPostal', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombreCiudad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idProvincia', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombreProvincia', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('cuit', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('face', models.URLField()),
                ('insta', models.URLField()),
                ('web', models.URLField()),
                ('imagenPrincipal', models.ImageField(upload_to='')),
                ('imagenAdicional1', models.ImageField(upload_to='')),
                ('imagenAdicional2', models.ImageField(upload_to='')),
                ('imagenAdicional3', models.ImageField(upload_to='')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendas.Ciudad')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendas.Provincia'),
        ),
    ]
