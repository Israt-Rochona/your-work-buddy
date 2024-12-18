# Generated by Django 5.1.2 on 2024-11-06 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_id', models.IntegerField(max_length=100)),
                ('consumer_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact_info', models.IntegerField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('nid', models.IntegerField(max_length=200)),
                ('rating', models.FloatField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=200)),
                ('provider_id', models.IntegerField(max_length=20)),
                ('skills', models.TextField(max_length=1000)),
                ('certification', models.BooleanField(blank=True, null=True)),
                ('employement_type', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(max_length=20)),
                ('service_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate_per_hour', models.FloatField(max_length=300)),
                ('duration', models.IntegerField(max_length=200)),
                ('consumer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.consumer')),
                ('provider_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service_provider')),
            ],
        ),
    ]
