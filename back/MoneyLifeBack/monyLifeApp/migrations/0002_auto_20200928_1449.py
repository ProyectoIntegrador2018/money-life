# Generated by Django 3.0.7 on 2020-09-28 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monyLifeApp', '0001_initial'),
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
            name='Evento_Afect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('id_Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento')),
            ],
            options={
                'unique_together': {('id_Afecta', 'id_Evento')},
            },
        ),
        migrations.CreateModel(
            name='Evento_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento')),
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
            name='Preguntas_Afecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('id_Preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas')),
            ],
            options={
                'unique_together': {('id_Afecta', 'id_Preguntas')},
            },
        ),
        migrations.CreateModel(
            name='Preguntas_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadRecurente', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas')),
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
            name='Prestamo_Afect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('id_Prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo')),
            ],
            options={
                'unique_together': {('id_Afecta', 'id_Prestamo')},
            },
        ),
        migrations.CreateModel(
            name='Prestamo_Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadRecurente', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('id_Prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo')),
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
                ('Afecta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Afecta')),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Evento')),
                ('Preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Preguntas')),
                ('Prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Prestamo')),
                ('Requisitos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RolUsuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
        migrations.DeleteModel(
            name='Prueba2',
        ),
        migrations.AddField(
            model_name='turnos',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.User'),
        ),
        migrations.AddField(
            model_name='prestamo_requisitos',
            name='id_Requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.User'),
        ),
        migrations.AddField(
            model_name='preguntas_requisitos',
            name='id_Requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.User'),
        ),
        migrations.AddField(
            model_name='evento_requisitos',
            name='id_Requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='Afecta',
            field=models.ManyToManyField(through='monyLifeApp.Evento_Afect', to='monyLifeApp.Afecta'),
        ),
        migrations.AddField(
            model_name='evento',
            name='Requisitos',
            field=models.ManyToManyField(through='monyLifeApp.Evento_Requisitos', to='monyLifeApp.Requisitos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monyLifeApp.User'),
        ),
        migrations.AlterUniqueTogether(
            name='prestamo_requisitos',
            unique_together={('id_Requisito', 'id_Prestamo')},
        ),
        migrations.AlterUniqueTogether(
            name='preguntas_requisitos',
            unique_together={('id_Requisito', 'id_Preguntas')},
        ),
        migrations.AlterUniqueTogether(
            name='evento_requisitos',
            unique_together={('id_Requisito', 'id_Evento')},
        ),
    ]