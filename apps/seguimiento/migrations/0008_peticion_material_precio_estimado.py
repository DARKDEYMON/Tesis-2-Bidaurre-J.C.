# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0007_auto_20161001_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='peticion_material',
            name='precio_estimado',
            field=models.PositiveIntegerField(default=50),
            preserve_default=False,
        ),
    ]
