# Generated by Django 3.2.18 on 2023-09-25 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiducia', '0002_initial'),
        ('asset', '0011_auto_20230925_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoinversion',
            name='fiducia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fiducia.fiducia'),
        ),
    ]