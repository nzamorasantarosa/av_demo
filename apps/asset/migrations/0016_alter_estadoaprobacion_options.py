# Generated by Django 3.2.18 on 2023-09-26 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0015_activoinversion_estado_aprobacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estadoaprobacion',
            options={'ordering': ['paso']},
        ),
    ]
