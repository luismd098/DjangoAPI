# Generated by Django 5.0.2 on 2024-02-12 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BitaServices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('AreaId', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('TipoArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('BitacoraId', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('NumeroEquipo', models.IntegerField(default=0, max_length=1)),
                ('Modelo', models.CharField(max_length=50)),
                ('Version', models.CharField(max_length=50)),
                ('FechaCreacion', models.DateField()),
                ('Activo', models.IntegerField(max_length=1)),
                ('AreaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitaServices.area')),
            ],
        ),
        migrations.CreateModel(
            name='EstatusReporte',
            fields=[
                ('EstatusReporteId', models.AutoField(primary_key=True, serialize=False)),
                ('Color', models.CharField(max_length=20)),
                ('DescripcionCorta', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('LicenciaId', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=200)),
                ('FechaCreacion', models.DateField()),
                ('Activo', models.IntegerField(default=1, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Privilegio',
            fields=[
                ('PrivilegioId', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Eliminar', models.IntegerField(max_length=1)),
                ('Agregar', models.IntegerField(max_length=1)),
                ('Editar', models.IntegerField(max_length=1)),
                ('FechaCreacion', models.DateField()),
                ('Activo', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RelBitacoraLicencia',
            fields=[
                ('RelId', models.AutoField(primary_key=True, serialize=False)),
                ('Activo', models.IntegerField(default=1, max_length=1)),
                ('FechaCreacion', models.DateField()),
                ('FechaActualizacion', models.DateField()),
                ('BitacoraId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BitaServices.bitacora')),
                ('LicenciaId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BitaServices.licencia')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('ReporteId', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=1000)),
                ('FechaCreacion', models.DateField()),
                ('Activo', models.IntegerField(default=1, max_length=1)),
                ('BitacoraId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitaServices.bitacora')),
                ('EstatusReporteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitaServices.estatusreporte')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('UsuarioId', models.AutoField(primary_key=True, serialize=False)),
                ('Usuario', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('FCreacion', models.DateField()),
                ('Activo', models.IntegerField(default=1, max_length=1)),
                ('PrivilegioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitaServices.privilegio')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
