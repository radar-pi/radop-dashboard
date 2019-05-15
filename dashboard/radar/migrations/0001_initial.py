# Generated by Django 2.0.13 on 2019-05-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Nome do Radar')),
                ('identificacao', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Identificação do Radar')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
            ],
            options={
                'verbose_name': 'Radar',
                'verbose_name_plural': 'Radares',
            },
        ),
    ]