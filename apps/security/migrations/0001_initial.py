# Generated by Django 3.2.18 on 2024-10-11 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_change_frecuency', models.PositiveIntegerField(default=30)),
                ('password_similarity_limit', models.PositiveIntegerField(default=5)),
                ('max_failed_login_attempts', models.PositiveIntegerField(default=3)),
                ('login_lockout_duration', models.DurationField(default=datetime.timedelta(seconds=1800))),
                ('password_expiry_days', models.PositiveIntegerField(default=90)),
                ('password_max_delta_change', models.DurationField(default=datetime.timedelta(seconds=1800))),
            ],
        ),
    ]