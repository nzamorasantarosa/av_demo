# Generated by Django 3.2.18 on 2023-11-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0032_activoinversion_id_contrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoinversion',
            name='metadata_smartcontract',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
