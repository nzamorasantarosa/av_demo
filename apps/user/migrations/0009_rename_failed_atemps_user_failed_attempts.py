# Generated by Django 3.2.18 on 2023-11-16 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_failed_atemps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='failed_atemps',
            new_name='failed_attempts',
        ),
    ]