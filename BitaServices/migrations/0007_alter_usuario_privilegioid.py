# Generated by Django 5.0.2 on 2024-02-14 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BitaServices', '0006_alter_usuario_privilegioid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='PrivilegioId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitaServices.privilegio'),
        ),
    ]