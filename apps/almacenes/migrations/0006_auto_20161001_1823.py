# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0005_auto_20161001_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='ciudad',
            field=models.CharField(choices=[('PT', 'Potosi'), ('LP', 'La Paz'), ('CO', 'Cochabamba'), ('CH', 'Chuquisaca'), ('TA', 'Tarija'), ('OR', 'Oruro'), ('SC', 'Santa Cruz'), ('BE', 'Beni'), ('PA', 'Pando')], max_length=100, unique=True),
        ),
    ]
