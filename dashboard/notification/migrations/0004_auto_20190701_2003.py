# Generated by Django 2.0.13 on 2019-07-01 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20190630_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='penalty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.Penalty'),
        ),
    ]
