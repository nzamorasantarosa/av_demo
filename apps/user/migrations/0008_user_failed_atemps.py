# Generated by Django 3.2.18 on 2023-11-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_last_password_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='failed_atemps',
            field=models.IntegerField(default=0),
        ),
    ]