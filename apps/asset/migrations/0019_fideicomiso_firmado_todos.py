# Generated by Django 3.2.18 on 2023-09-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0018_fideicomiso_response_weetrust'),
    ]

    operations = [
        migrations.AddField(
            model_name='fideicomiso',
            name='firmado_todos',
            field=models.BooleanField(default=False),
        ),
    ]