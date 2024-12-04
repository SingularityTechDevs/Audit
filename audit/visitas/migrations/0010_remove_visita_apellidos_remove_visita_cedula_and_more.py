# Generated by Django 4.1.1 on 2024-05-26 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0009_cita_estatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='fecha_visita',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='telefonos',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='tipo_visita',
        ),
        migrations.AddField(
            model_name='cita',
            name='apellidos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='cedula',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='fecha_visita',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 20, 14, 9, 519066)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cita',
            name='nombres',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='sexo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='telefonos',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='tipo_visita',
            field=models.CharField(choices=[('Pre-empleo', 'Pre-empleo'), ('Mantenimiento', 'Mantenimiento'), ('Aleatoria', 'Aleatoria')], default=datetime.datetime(2024, 5, 26, 20, 15, 20, 763831), max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('año', models.PositiveIntegerField()),
                ('modo_adquisicion', models.CharField(max_length=100)),
                ('tiempo_con_vehiculo', models.CharField(max_length=100)),
                ('visitas', models.ManyToManyField(blank=True, null=True, to='visitas.cita')),
            ],
        ),
    ]