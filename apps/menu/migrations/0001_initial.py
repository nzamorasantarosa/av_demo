# Generated by Django 3.2.18 on 2023-09-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'permissions': [('user_ver_activos', 'Usuario puede ver activos'), ('user_upload_fideicomiso', 'Usuario puede cargar fideicomisos'), ('user_consultar_movimientos', 'Usuario puede consultar movimientos'), ('user_ver_inversionistas', 'Usuario puede ver inversionistas')],
            },
        ),
    ]
