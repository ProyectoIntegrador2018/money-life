# Generated by Django 3.1.2 on 2020-11-14 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monyLifeApp', '0004_auto_20201114_0201'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evento_user',
            unique_together=set(),
        ),
    ]
