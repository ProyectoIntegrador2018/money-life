# Generated by Django 3.0.7 on 2020-10-08 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monyLifeApp', '0004_afecta_evento_requisitos_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Afecta',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Requisitos',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]