# Generated by Django 4.0 on 2021-12-19 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('storage_temp', models.CharField(max_length=100)),
                ('reference_num', models.CharField(max_length=100)),
                ('part_number', models.CharField(max_length=100)),
                ('unit_of_measure', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('lot_number', models.IntegerField()),
                ('expiration_date', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
