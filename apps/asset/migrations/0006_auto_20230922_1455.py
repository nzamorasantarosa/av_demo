# Generated by Django 3.2.18 on 2023-09-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_alter_activoinversion_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='correo_enviado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='email_devise',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='email_fiducia',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='email_propietario',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='email_sponsor',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='name_devise',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='name_fiducia',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='name_propietario',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='constitucionfideicomiso',
            name='name_sponsor',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
