# Generated by Django 3.0.7 on 2020-10-08 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monyLifeApp', '0002_auto_20201004_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='TipoPregunta',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='User',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='TipoPrestamo',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='User',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='Evento',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='Preguntas',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='Prestamo',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='User',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.DeleteModel(
            name='Tipo_Evento',
        ),
        migrations.DeleteModel(
            name='Tipo_Pregunta',
        ),
        migrations.DeleteModel(
            name='Tipo_Prestamo',
        ),
        migrations.DeleteModel(
            name='Turnos',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
