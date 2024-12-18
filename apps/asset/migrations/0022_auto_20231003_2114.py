# Generated by Django 3.2.18 on 2023-10-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0021_auto_20231003_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activoinversion',
            name='clase_inversion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='incremento_anual',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='no_id_fideicomiso',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='nombre_fideicomiso',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='pago_rendimiento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='plazo_contrato',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='activoinversion',
            name='tenencia_sugerida',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fideicomiso',
            name='devise_biometric_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fideicomiso',
            name='fiducia_biometric_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fideicomiso',
            name='propietario_biometric_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fideicomiso',
            name='sponsor_biometric_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
