# Generated by Django 3.2.18 on 2023-09-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_activoinversion_fiducia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activoinversion',
            options={'permissions': [('approved_activo_devise', 'Puede aprobar activo para la Devise'), ('approved_activo_fiducia', 'Puede aprobar activo para la Fiducia')]},
        ),
    ]
