# Generated by Django 3.2.18 on 2023-09-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activoinversion',
            name='estado_aprobacion',
            field=models.CharField(blank=True, choices=[('Activo pendiente aprobacion Sponsor', 'Activo pendiente aprobacion Sponsor '), ('Pendiente respuesta del Propietario', 'Pendiente respuesta del Propietario'), ('Activo aprobado por el Sponsor', 'Activo aprobado por el Sponsor'), ('Pendiente respuesta del Sponsor', 'Pendiente respuesta del Sponsor'), ('Activo aprobado por Devise', 'Activo aprobado por Devise')], max_length=126, null=True),
        ),
    ]