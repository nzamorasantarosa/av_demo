# Generated by Django 3.2.18 on 2024-04-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaleido', '0006_walletsmartcontract'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletsmartcontract',
            name='type_wallet',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]