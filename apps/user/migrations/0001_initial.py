# Generated by Django 3.2.18 on 2023-09-08 15:57

import apps.user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('notaria', '0001_initial'),
        ('fiducia', '0002_initial'),
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='correo electrónico')),
                ('indicative', models.CharField(max_length=32, verbose_name='indicativo')),
                ('phone', models.CharField(max_length=64, verbose_name='teléfono')),
                ('is_natural_person', models.BooleanField(default=True)),
                ('juridic_xlsx', models.FileField(blank=True, null=True, upload_to=apps.user.models.owner_file_path)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('document_number', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('document_front_image', models.ImageField(upload_to=apps.user.models.owner_file_path)),
                ('document_back_image', models.ImageField(blank=True, null=True, upload_to=apps.user.models.owner_file_path)),
                ('selfie', models.ImageField(blank=True, null=True, upload_to=apps.user.models.owner_file_path)),
                ('expedition_date', models.DateField(blank=True, null=True)),
                ('kyc_validated', models.CharField(choices=[('pending_document', 'Pendiente por cargar documento'), ('ready_for_kyc', 'Pendiente por subir a KYC'), ('validating_document', 'Documento en Validación'), ('fail_document', 'Fallo en Documento'), ('sucessfull_document', 'KYC Validado')], default='pending_document', max_length=64)),
                ('mail_delivery', models.CharField(blank=True, choices=[('E-MAIL', 'Correo Electronico'), ('DOMICILIO', 'A la Dirección del Domicilio'), ('TRABAJO', 'A la Direccion del Trabajo')], max_length=126, null=True)),
                ('code', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('referred_by_code', models.CharField(blank=True, max_length=128, null=True)),
                ('slug', models.SlugField(blank=True)),
                ('birth_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='birth_city', to='cities_light.subregion')),
                ('birth_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='birth_country', to='cities_light.country')),
                ('birth_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='birth_region', to='cities_light.region')),
                ('doc_city_expedition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.subregion')),
                ('doc_country_expedition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.country')),
                ('doc_region_expedition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.region')),
                ('fiducia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fiducia.fiducia')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            managers=[
                ('objects', apps.user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('value', models.CharField(max_length=126)),
                ('name', models.CharField(max_length=126)),
                ('description', models.CharField(max_length=126)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=126)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('recovery_code', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='local_id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.idtype'),
        ),
        migrations.AddField(
            model_name='user',
            name='notaria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='notaria.notaria'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('indicative', 'phone')},
        ),
    ]