# Generated by Django 3.2.7 on 2021-11-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_auto_20211108_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activo',
            field=models.CharField(max_length=1, null=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefono'),
        ),
    ]
