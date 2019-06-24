# Generated by Django 2.0.13 on 2019-06-24 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_track_speed', models.IntegerField(blank=True, default=0)),
                ('considered_speed', models.IntegerField(blank=True, default=0)),
                ('crash_feasability', models.FloatField(blank=True, default=0.0)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('infraction_identifier', models.CharField(max_length=36)),
                ('identifier', models.CharField(max_length=36)),
                ('notification_type', models.CharField(blank=True, choices=[('INFRACAO', 'Infração'), ('POSSIVEL', 'Possível Acidente')], default='INFRACAO', max_length=17)),
                ('read_speed', models.IntegerField(blank=True, default=0)),
                ('time', models.CharField(blank=True, max_length=8)),
                ('vehicle_brand', models.CharField(blank=True, max_length=200)),
                ('vehicle_chassi', models.CharField(blank=True, max_length=200)),
                ('vehicle_city', models.CharField(blank=True, max_length=500)),
                ('vehicle_color', models.CharField(blank=True, max_length=200)),
                ('vehicle_model', models.CharField(blank=True, max_length=200)),
                ('vehicle_plate', models.CharField(blank=True, max_length=7)),
                ('vehicle_state', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2)),
                ('vehicle_status', models.CharField(blank=True, max_length=200)),
                ('vehicle_year', models.CharField(blank=True, max_length=4)),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('MEDIA', 'Média'), ('SEVERE', 'Grave'), ('EXTREME SEVERE', 'Gravíssima')], default='MEDIA', max_length=14)),
                ('points', models.IntegerField(default=3)),
                ('value', models.FloatField(default=130.16)),
            ],
            options={
                'verbose_name': 'Multa',
                'verbose_name_plural': 'Multas',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='penalty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='notification.Penalty'),
        ),
    ]
