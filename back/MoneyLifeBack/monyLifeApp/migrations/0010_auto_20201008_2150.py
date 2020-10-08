# Generated by Django 3.0.7 on 2020-10-08 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monyLifeApp', '0009_auto_20201008_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoAfect', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoEvento', models.CharField(max_length=30)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Frecuencia', models.IntegerField()),
                ('Probabilidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoPregunta', models.CharField(max_length=30)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Probabilidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoPrestamo', models.CharField(max_length=30)),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Intereses', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoRequisito', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroTurnos', models.IntegerField()),
                ('Felicidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('DineroEfectivo', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Ingresos', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Egresos', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Edad', models.IntegerField()),
                ('Sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RolUsuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos')),
                ('Turnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Turnos')),
            ],
            options={
                'unique_together': {('Requisito', 'Turnos')},
            },
        ),
        migrations.CreateModel(
            name='Turnos_Afecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('Turnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Turnos')),
            ],
            options={
                'unique_together': {('Afecta', 'Turnos')},
            },
        ),
        migrations.AddField(
            model_name='turnos',
            name='Afecta',
            field=models.ManyToManyField(through='monyLifeApp.Turnos_Afecta', to='monyLifeApp.Afecta'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='Evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='Preguntas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='Prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='Requisitos',
            field=models.ManyToManyField(through='monyLifeApp.Turnos_Requisitos', to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monyLifeApp.User'),
        ),
        migrations.CreateModel(
            name='Prestamo_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadRecurente', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo')),
                ('Requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos')),
            ],
            options={
                'unique_together': {('Requisito', 'Prestamo')},
            },
        ),
        migrations.CreateModel(
            name='Prestamo_Afect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('Prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo')),
            ],
            options={
                'unique_together': {('Afecta', 'Prestamo')},
            },
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Afecta',
            field=models.ManyToManyField(through='monyLifeApp.Prestamo_Afect', to='monyLifeApp.Afecta'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Requisitos',
            field=models.ManyToManyField(through='monyLifeApp.Prestamo_Requisitos', to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monyLifeApp.User'),
        ),
        migrations.CreateModel(
            name='Preguntas_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadRecurente', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas')),
                ('Requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos')),
            ],
            options={
                'unique_together': {('Requisito', 'Preguntas')},
            },
        ),
        migrations.CreateModel(
            name='Preguntas_Afecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('Preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas')),
            ],
            options={
                'unique_together': {('Afecta', 'Preguntas')},
            },
        ),
        migrations.AddField(
            model_name='preguntas',
            name='Afecta',
            field=models.ManyToManyField(through='monyLifeApp.Preguntas_Afecta', to='monyLifeApp.Afecta'),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='Requisitos',
            field=models.ManyToManyField(through='monyLifeApp.Preguntas_Requisitos', to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monyLifeApp.User'),
        ),
        migrations.CreateModel(
            name='Evento_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento')),
                ('Requisito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos')),
            ],
            options={
                'unique_together': {('Requisito', 'Evento')},
            },
        ),
        migrations.CreateModel(
            name='Evento_Afecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento')),
            ],
            options={
                'unique_together': {('Afecta', 'Evento')},
            },
        ),
        migrations.AddField(
            model_name='evento',
            name='Afecta',
            field=models.ManyToManyField(through='monyLifeApp.Evento_Afecta', to='monyLifeApp.Afecta'),
        ),
        migrations.AddField(
            model_name='evento',
            name='Requisitos',
            field=models.ManyToManyField(through='monyLifeApp.Evento_Requisitos', to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monyLifeApp.User'),
        ),
    ]
