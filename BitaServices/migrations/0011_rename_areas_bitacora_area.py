# Generated by Django 5.0.2 on 2024-02-17 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BitaServices', '0010_rename_areaid_bitacora_areas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bitacora',
            old_name='Areas',
            new_name='Area',
        ),
    ]
