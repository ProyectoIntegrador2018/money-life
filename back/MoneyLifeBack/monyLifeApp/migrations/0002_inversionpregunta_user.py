# Generated by Django 3.1.2 on 2020-11-13 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monyLifeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversionpregunta',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
