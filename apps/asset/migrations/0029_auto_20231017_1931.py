# Generated by Django 3.2.18 on 2023-10-18 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0028_alter_feedbackminutaescrituracion_minuta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackminutaescrituracion',
            name='mensaje',
            field=models.TextField(default='Mensje'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedbackminutaescrituracion',
            name='minuta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='asset.minutaescrituracion'),
            preserve_default=False,
        ),
    ]
